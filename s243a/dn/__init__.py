import urllib2,sys,re,os,urllib,os.path
from SoupDefaults import *

from bs4 import BeautifulSoup
rootPath = r"/root/projects/pytest/"
#https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run
if not (rootPath in sys.path):
    print("Appending "+rootPath)
    sys.path.append(rootPath)
from s243a.dn.dn_util import *
from s243a.dn.dn_show import *
from s243a.dn import *
from s243a.fn import *

#<a data-ga-action="Show Preview: Story" href="/2018/12/27/without_notifying_anyone_ice_dumps_hundreds" tabindex="0">
#  <div class="media image">
#    <img class="modern" src="https://www.democracynow.org/images/story/02/45402/w320/SEG_ICE-DumpingMigrants-ElPaso-3.jpg"
#      alt="Seg ice dumpingmigrants elpaso 3">
#  </div>
#   <h3>Without Notifying Anyone, <span class="caps">ICE</span> Dumps Hundreds of Migrants at El Paso Bus Station Around Christmas</h3>
#</a>



class DN_Show_Listener_Cpy2File:
    def __init__(self,**kw):
        self.urlRoot=kw.get('urlRoot','/')
        self.saveRoot=kw.get('saveRoot','/tmp/DN')
        self.protocol=kw.get('protocol','http')
        self.domain=kw.get('domain','www.democracynow.org')
    def on_show(self,all_shows,kw):
        show=all_shows[-1]
        #for html_attr in ('href','src','alt','title')
                
        #Make image direcotry and save image
        src=getAttrOrVal(show,'src')
        src=iff_nc(src is None,kw['src'],src)
        (src_path,src_bname)=getURLPart(src,'path','bname') #TODO think up a better name for this function.
        src_save_path=""+self.saveRoot+"/"+stripRoot(src_path,self.urlRoot)
        mkdir(src_save_path)
        full_path = src_save_path+"/"+src_bname
        print("src="+str(src))
        print("full_path="+full_path)
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
    print('href='+href)
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

def default_on_append(shows,kw):
    shows.append(
      DN_show(**kw)
    )
def default_get_show_KWs(show):
  kw2={'href' : show.a.attrs['href'],
       'src'  : show.div.img.attrs['src'],
       'alt'  : show.div.img.attrs['alt'],    
       'title': show.div.h3.text}
  return kw2
read_DN_shows_defaults={
  'url':'https://www.democracynow.org/shows',  
  'readURL':lambda url: urllib2.urlopen(url),
  'getPage_factory': lambda readURL,url: lambda: readURL(url),
  'getSoup_factory':lambda kw,getPage: \
      lazyGet(kw,'getSoup',
                 lambda: BeautifulSoup(getPage()))} 

 
shows=[]                 
def read_DN_shows(**kw):
  #url='https://www.democracynow.org/shows'
  #page = urllib2.urlopn(url) 
  #soup = BeautifulSoup(page)
  #all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})
  defaults=kw.get('defaults',read_DN_shows_defaults)
  saveRoot=kw.get('saveRoot','/home/freenet/jsite/dn')
  url=kw.get('url',defaults['url'])
  readURL=kw.get('readURL',defaults['readURL'])
  getPage=kw.get('getPage',defaults['getPage_factory'](readURL,url))
  getSoup=lazyGet(kw,'getSoup',
               defaults['getSoup_factory'](kw,getPage))
  #print(str(getSoup))             
  all_stories=alt_fn(kw,'all_stories',
                         defaults['all_stories_factory'](getSoup))
  #print("Printine all_stories")
  #print(str(all_stories))
  all_shows=kw.get('out',shows)
  listeners=kw.get('listeners',[])
  if 'on_append' in kw:
      if kw['on_append'] is not None:
           listeners.insert(0,kw['on_append'])
  else:
      listeners.insert(0,lambda a,b: default_on_append(a,b))
  #print("printing all_stories")
  #print(str(all_stories))        
  for show_raw in all_stories:
    #print("type of show_raw="+str(type(show_raw)))
    show=show_raw
    #print("Printing show")
    #print(show)
    #print("printing show.a")
    #print(show.a)
    kw2={'href' : show.get('href'),
         'src'  : show.div.img.attrs['src'],
         'alt'  : show.div.img.attrs['alt'] ,   
         'title': show.h3.text}
    for listener in listeners:
      #all_shows.append(
      #  DN_show(href=href,src=src,text=text,alt=alt)
      #)    
      if hasattr(listener,'on_show'):
          listener.on_show(all_shows,kw2)
      elif callable(listener):
          listener(all_shows,kw2)
  mkIndex(all_shows,saveRoot)
saveRoot="/home/freenet/jsite/dn"
no_refresh=True
listeners=[DN_Show_Listener_Cpy2File(urlRoot="/",saveRoot=saveRoot,no_refresh=no_refresh)]
read_DN_shows(listeners=listeners,defaults=DN_shows_defaults,saveRoot=saveRoot)
            
    
