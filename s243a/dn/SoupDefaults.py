import urllib2
from bs4 import BeautifulSoup
#  'getSoup_factory':lambda kw,getPage: \
#      lazyGet(kw,'getSoup',
#                 lambda: BeautifulSoup(getPage()))}  
def DN_getSoup_Factory(kw,getPage):
    if 'getSoup' in kw:
        return getSoup
    else:
        page=getPage()
        #print(page)
        soup=BeautifulSoup(page,features="html.parser")
        #print('printing soup')
        #print(soup)
        return lambda: soup
#all_stories=soup.find_all('a',{'data-ga-action':'Show Preview: Story'})
def dn_all_stories_factory(getSoup):
    all_stories=getSoup().find_all('a',{'data-ga-action':'Show Preview: Story'})
    print("Printing all_stories")
    print(all_stories)
    return lambda: all_stories
DN_shows_defaults={\
  'url':'https://www.democracynow.org/shows',  
  'readURL':lambda url: urllib2.urlopen(url),
  'getPage_factory': lambda readURL,url: lambda: readURL(url),
  'getSoup_factory':DN_getSoup_Factory,
  'all_stories_factory':dn_all_stories_factory} 