import urllib2,sys,pdb
from bs4.element import ResultSet
from bs4 import BeautifulSoup
rootPath = r"/root/projects/pytest/"
#https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run
if not (rootPath in sys.path):
    #print("Appending "+rootPath)
    sys.path.append(rootPath)
from s243a.fn import *    
#  'getSoup_factory':lambda kw,getPage: \
#      lazyGet(kw,'getSoup',
#                 lambda: BeautifulSoup(getPage()))}  
def DN_getSoup_Factory(kw,getPage):
    if 'getSoup' in kw: #??????????????
        return getSoup
    else:
        page=safeCall(getPage)
        #print(page)
        soup=BeautifulSoup(page,features="html.parser")
        #print('printing soup')
        #print(soup)
        #print("Type="+str(type(soup)))
        return lambda: soup
#all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})
def dn_all_shows_factory(getSoup):
    #soup=safeCall(getSoup)
    
    if not isinstance(getSoup,BeautifulSoup):
        soup=getSoup()  
    else:
        soup=getSoup
    all_shows=soup.find_all('div',{'class':'show_preview'})
    #print("Printing all_shows")
    #print(all_shows)
    return lambda: all_shows
def dn_all_stories_factory(getSoup):
    #soup=safeCall(getSoup)
    if not isinstance(getSoup,BeautifulSoup):
        soup=getSoup()
        
    else:
        soup=getSoup
    #print("Type="+str(type(soup)))
    #print(str(soup))
    #print(str(soup))
    #print("Type="+str(type(soup)))
    #all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})
    if isinstance(soup,BeautifulSoup):
        all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})
    else:
        #https://wooptoo.com/blog/scraping-with-beautifulsoup/
        
        #L=[s.find('a',{'data-ga-action':'Show Preview: Story'}) for s in soup]
        #all_stories=[x for x in L if x is not None]
        #all_stories=ResultSet()
        L=[]
        print("soup="+str(soup))
        pdb.set_trace()
        for tag in soup:
            #tag2=tag.find('a',{'data-ga-action':'Show Preview: Story'})
            #if tag2 is not None:
            #    L.append(tag2)                
            #    print("L="+str(tag2))
            #    pdb.set_trace()
            if (tag.name=="a") and (tag.attrs['data-ga-action']=="Show Preview: Story"):
               L.append(tag)
        all_stories=L #ResultSet(L) we really don't need result set.    
        #print(str(all_stories))
        #print(Type=
        #pdb.set_trace()
    #print("Printing all_stories")
    #print(all_stories)
    return lambda: all_stories
#read_DN_shows_defaults={
#  'url':'https://www.democracynow.org/shows',  
#  'readURL':lambda url: urllib2.urlopen(url),
#  'getPage_factory': lambda readURL,url: lambda: readURL(url),
#  'getSoup_factory':lambda kw,getPage: \
#      lazyGet(kw,'getSoup',
#                 lambda: BeautifulSoup(getPage()))}     
DN_shows_defaults={\
  'url':'https://www.democracynow.org/shows',  
  'readURL':lambda url: urllib2.urlopen(url),
  'getPage_factory': lambda readURL,url: lambda: readURL(url),
  'getSoup_factory':DN_getSoup_Factory,
  'all_stories_factory':dn_all_stories_factory,
  'all_shows_factory':dn_all_shows_factory} 
default_story_to_dict=lambda story:\
  {'href' : story.get('href'),
   'src'  : story.div.img.attrs['src'],
   'alt'  : story.div.img.attrs['alt'] ,   
   'title': story.h3.text}
def default_get_story_KWs(story,show_obj=None):
  kw2={'href' : story.get('href'),
       'src'  : story.div.img.attrs['src'],
       'alt'  : story.div.img.attrs['alt'],    
       'title': story.h3.text,
       'show_obj':show_obj}
  return kw2