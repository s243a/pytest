DN_shows_defaults_old={\
  'url':'https://www.democracynow.org/shows',  
  'readURL':lambda url: urllib2.urlopen(url),
  'getPage_factory': lambda readURL,url: lambda: readURL(url),
  'getSoup_factory':DN_getSoup_Factory,
  'all_stories_factory':dn_all_stories_factory} 
read_DN_shows_defaults_old={
  'url':'https://www.democracynow.org/shows',  
  'readURL':lambda url: urllib2.urlopen(url),
  'getPage_factory': lambda readURL,url: lambda: readURL(url),
  'getSoup_factory':lambda kw,getPage: \
      lazyGet(kw,'getSoup',
                 lambda: BeautifulSoup(getPage()))} 
def read_DN_shows(**kw):

  defaults=kw.get('defaults',read_DN_shows_defaults_old)
  saveRoot=kw.get('saveRoot','/home/freenet/jsite/dn')
  url=kw.get('url',defaults['url'])
  readURL=kw.get('readURL',defaults['readURL'])
  getPage=kw.get('getPage',defaults['getPage_factory'](readURL,url))
  getSoup=lazyGet(kw,'getSoup',
               defaults['getSoup_factory'](kw,getPage))           
  all_stories=alt_fn(kw,'all_stories',
                         defaults['all_stories_factory'](getSoup))
  story_to_dict=kw.get('story_to_dict',default_story_to_dict)
  get_story_KWs=kw.get('get_story_KWs',default_get_story_KWs)
  all_stories=kw.get('all_stories',[])
  listeners=kw.get('listeners',[])
  if 'on_append' in kw:
      if kw['on_append'] is not None:
           listeners.insert(0,kw['on_append'])
  else:
      listeners.insert(0,lambda a,b: default_on_append(a,b))
     
  for story in all_stories:
    #kw2={'href' : story.get('href'),
    #     'src'  : story.div.img.attrs['src'],
    #     'alt'  : story.div.img.attrs['alt'] ,   
    #     'title': story.h3.text}
    kw2=get_story_KWs(story)
    for listener in listeners:

      if hasattr(listener,'on_story'):
          listener.on_story(all_stories,kw2)
      elif callable(listener):
          listener(all_stories,kw2)
  mkIndex(all_stories,saveRoot)
  saveRoot="/home/freenet/jsite/dn"
#no_refresh=True
#listeners=[DN_Story_Listener_Cpy2File(urlRoot="/",saveRoot=saveRoot,no_refresh=no_refresh)]
#read_DN_Stories(listeners=listeners,defaults=DN_Stories_defaults_old,saveRoot=saveRoot)