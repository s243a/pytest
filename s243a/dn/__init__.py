import urllib2,sys,re,os,urllib,os.path
from unidecode import unidecode
from SoupDefaults import *

from bs4 import BeautifulSoup
rootPath = r"/root/projects/pytest/"
#https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run
if not (rootPath in sys.path):
    print("Appending "+rootPath)
    sys.path.append(rootPath)
from s243a.fn import *    
#from s243a.fn import safeCall    
from s243a.dn.dn_util import *
from s243a.dn.dn_show import *
from s243a.dn import *



#<a data-ga-action="Show Preview: Story" href="/2018/12/27/without_notifying_anyone_ice_dumps_hundreds" tabindex="0">
#  <div class="media image">
#    <img class="modern" src="https://www.democracynow.org/images/story/02/45402/w320/SEG_ICE-DumpingMigrants-ElPaso-3.jpg"
#      alt="Seg ice dumpingmigrants elpaso 3">
#  </div>
#   <h3>Without Notifying Anyone, <span class="caps">ICE</span> Dumps Hundreds of Migrants at El Paso Bus Station Around Christmas</h3>
#</a>



class DN_Story_Listener_Cpy2File:
    def __init__(self,**kw):
        self.urlRoot=kw.get('urlRoot','/')
        self.saveRoot=kw.get('saveRoot','/tmp/DN')
        self.protocol=kw.get('protocol','http')
        self.domain=kw.get('domain','www.democracynow.org')
    def on_story(self,all_shows_out,kw):
        show=all_shows_out[-1]
        #for html_attr in ('href','src','alt','title')
                
        #Make image direcotry and save image
        src=getAttrOrVal(show,'src')
        src=iff_nc(src is None,kw['src'],src)
        (src_path,src_bname)=getURLPart(src,'path','bname') #TODO think up a better name for this function.
        src_save_path=""+self.saveRoot+"/"+stripRoot(src_path,self.urlRoot)
        mkdir(src_save_path)
        full_path = src_save_path+"/"+src_bname
        #print("src="+str(src))
        #print("full_path="+full_path)
        no_refresh
        if (not os.path.exists(full_path)) or (no_refresh==False): 
            urllib.urlretrieve( str(src), full_path )
        
        #Make article direcotry and save article:
        href=getAttrOrVal(show,'href')
        href=iff_nc(href is None,kw['href'],href)
        
        (href_protocol,href_domain,\
         href_path,    href_bname)=\
            getURLPart(href,'protocol','domain','path','bname') 
        href_save_path=""+self.saveRoot+"/"+stripRoot(href_path,self.urlRoot)        
        mkdir(href_save_path)
        if href_bname is None:
            href_bname2=""
        else:
            href_bname2=href_bname
        if href_protocol is None:
            href_full=self.protocol+"://"+self.domain+"/"+stripRoot(href_path,"/")+"/"+href_bname2 #TODO make the protocol more dynamic
        else:
            href_full=href
        if href_bname is None:
            href_bname3='index.hml'
        else:
            href_bname3=href_bname        
        #soup_filter=lambda soup: soup.find_all('div',{'id':'story_content'})[0]
        full_save_path=""+href_save_path+"/"+href_bname3
        if (not os.path.exists(full_save_path)) or (no_refresh==False): 
            soup_filter=lambda soup: soup.find_all('div',{'id':'transcript'})[0]
            mkPage(href_full,full_save_path,soup_filter)
        
         #all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})

def writeBodyFmSoupFilter(f,href,soup_filter):
      #url='https://www.democracynow.org/shows'
    #print('href='+href)
    page = urllib2.urlopen(href) 
    soup = BeautifulSoup(page)
    all_stories=soup_filter(soup)
    f.write(str(all_stories))

def mkPage(href,href_save_path,soup_filter):
    with open(href_save_path, 'w+') as f:
        writeHTMLHeader(f)
        writeBodyFmSoupFilter(f,href,soup_filter)
        writeHTMLFooter(f)                


#      alt="Seg ice dumpingmigrants elpaso 3">

def default_on_append(stories,kw):
    story=DN_Story(**kw)
    stories.append(story)
    if 'show_obj' in kw:
      if kw['show_obj'] is not None:
        kw['show_obj'].append(story)
        print("appending story"+str(unidecode(story.to_HTML())))
      else:
        print("Show object is none")
        #pdb.set_trace()
    else:
      print("No show object")
      #pdb.set_trace()

#import dn_show
def read_DN_Stories(**kw):

  defaults=kw.get('defaults',DN_shows_defaults) #was read_DN_Stories_defaults
  saveRoot=kw.get('saveRoot','/home/freenet/jsite/dn')
  url=kw.get('url',defaults['url'])
  readURL=kw.get('readURL',defaults['readURL'])
  getPage=kw.get('getPage',defaults['getPage_factory'](readURL,url))
  getSoup=lazyGet(kw,'getSoup',
               defaults['getSoup_factory'](kw,getPage))
        
  all_shows_soup=safeCall(\
      alt_fn_nc(kw,'all_shows',
                    defaults['all_shows_factory']),
      getSoup)
  all_stories_soup=lambda getSoup=getSoup: \
      safeCall(\
          alt_fn_nc(kw,'all_stories',
                       defaults['all_stories_factory']),
          getSoup)
  story_to_dict=kw.get('story_to_dict',default_story_to_dict)
  get_story_KWs=kw.get('get_story_KWs',default_get_story_KWs)
  shows_out=kw.get('shows_out',[])
  stories_out=kw.get('stories_out',[])
  story_listeners=kw.get('listeners',[])
  if 'on_append' in kw:
      if kw['on_append'] is not None:
           story_listeners.insert(0,kw['on_append'])
  else:
      story_listeners.insert(0,lambda a,b: default_on_append(a,b))
      
  for show in itterator_or_None(all_shows_soup()):
    if show is not None:
        show_obj=DN_Show()  
        shows_out.append(show_obj)
        #print(str(show))
        #print("show.div="+str(show.div))
        #print("show.div[0].div[0]="+str(show.div[0].div[0]))
        #print("show.div[0].div[0].h5="+str(show.div[0].div[0].h5))
        date=show.div.div.h5.text
        print("date="+date)
        show_obj.date=date
    else:
        print("Show it not itterables")
        show=getSoup()
        #print("Type of show="+str(type(show)))
        show_obj=None
    for story in all_stories_soup(show):
      #print(str(story))  
      kw2=get_story_KWs(story,show_obj)
      for listener in story_listeners:

        if hasattr(listener,'on_story'):
            listener.on_story(stories_out,kw2)
        elif callable(listener):
            listener(stories_out,kw2)
  if len(shows_out)>0:          
      mkIndex(shows_out,saveRoot)
  else:
      mkIndex(stories_out,saveRoot)
saveRoot="/home/freenet/jsite/dn"
no_refresh=True
listeners=[DN_Story_Listener_Cpy2File(urlRoot="/",saveRoot=saveRoot,no_refresh=no_refresh)]
read_DN_Stories(listeners=listeners,defaults=DN_shows_defaults,saveRoot=saveRoot)
            
    
