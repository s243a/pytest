import sys,io

rootPath = r"/root/projects/pytest/"
#https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run
if not (rootPath in sys.path):
    print("Appending "+rootPath)
    sys.path.append(rootPath)
from s243a.util import *
from s243a.dn.dn_util import *
from s243a.dn import *


class DN_show:
    def __init__(self,**kw):
        self.href=DN_URL(kw.get('href',None))
        self.src=DN_URL(kw.get('src',None))
        self.title=kw.get('title',None)
        self.domain=DN_URL(kw.get('domain',None))
        self.alt=kw.get('alt',None)
        #self.new_domain=DN_URL(kw.get('new_domain','/'))       
        self.protocol=DN_URL(kw.get('protocol',None))               
        self.orig_domain=DN_URL(kw.get('original_domain',None))          
        self.root=kw.get('root',"/")
        self.orig_root=DN_URL(kw.get('original_root',"/"))        
        self.new_root=DN_URL(kw.get('new_domain',"dn"))        
        self.save_root=DN_URL(kw.get('save_root',"/home/freenet/jsite/dn"))
    def get_defaults(self,**kw):
        defaults={'root':self.root,'orig_root':self.orig_root,'save_root':self.save_root}
        itterator=getDictItterator(kw)
        for k,v in itterator:
            defaults[k]=v
        return defaults
    def localize_URL(self,curr_dir,url,*url_tags,**kw):
        defaults=self.get_defaults(**kw)
        for url_tag in ('src','href'):
            url=getattr(self,str(url_tag))            
            (protocol,domain,path,bname,rel_path,save_root)=\
                getURLPart(url,'protocol','domain','path','bname',
                               'relPath','save_root',**defaults) 
            print("save_root="+str(save_root))
            print("relPath="+str(rel_path))
            target_path=str(save_root)+"/"+str(rel_path)+"/"+bname #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if os.path.exists(target_path):
                url2=os.popen("realpath --relative-to='"+curr_dir+"' '"\
                                                        +target_path+"'"\
                             ).read().rstrip('\n')           
            else:
                url2=protocol+"://"+domain+"/"+path+"/"+bname
            self.set_url(url_tag,url2)
            #setattr(self,url_tag,url2)
    def set_url(self,atr,url,**kw):
        obj=getattr(self,atr)
        if hasattr(obj,'set_'+atr):
            setter=getattr(obj,atr)
            setter(url)
        elif hasattr(obj,atr):
            setattr(obj,atr,url)
        else:
            setattr(self,atr,url)
            
    def to_HTML(self):
        out=u'<a data-ga-action="Show Preview: Story" href='+str(self.href) + r' tabindex="0">' + \
            u'  <div class="media image">' + \
            u'    <img class="modern" src="' + str(self.src) + '" alt="' + str(self.alt) + '">' + \
            u'  </div>' + \
            u'  <h3>' + self.title +'</h3>' + \
            u'</a>'
        return out
        
class DN_URL:
    def __init__(self,url,**kw):
        self.url=url
        self.protocol=None
        self.domain=None
        self.path=None
        self.bname=None
        self.root=kw.get('root','/')
    def __str__(self):
        print("self.url="+self.url)
        return str(self.url)
    def parseURL(self):
        matches=parseURL(self.url)
        self.protocol=matches['protocol']
        self.domain=matches['domain']
        self.path=matches['path']
        self.bname=matches['bname']
    def get_protocol(self):
        if  self.protocol is None:
           self.parseURL()
        return self.protocol
    def get_domain(self):
        if  self.protocol is None:
           self.parseURL()
        return self.domain
    def get_bname(self):
        if  self.protocol is None:
           self.parseURL()
        return self.bname
    def get_path(self):
        if  self.protocol is None:
           self.parseURL()
        return self.path
    def get_relPath(self,root=None):
        if (root is None):
            root=self.root
        path=self.path
        first=path[0:len(root)]
        last=path[len(root):]
        if first==root:
            return last
        else:
            return first+last
            
def writeDN_Index_body(f,all_shows,saveRoot,curr_dir=None):
    if curr_dir==None:
        curr_dir=saveRoot
    for show in all_shows:
        #    def localize_URL(self,curr_dir,url,*url_tags,**kw): #TODO url_tags arg looks wierd
        show.localize_URL(curr_dir,show)
        f.write(show.to_HTML())
        f.write("\n"+'<br>'+"\n")
class Encoded_File_Wrapper:
    def __init__(self,f,encoding):
        self.f=f
        self.encoding=encoding
    def write(self,a_str):
        if isinstance(a_str, unicode):
            self.f.write(a_str)
        else:
            self.f.write(unicode(a_str, self.encoding))
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        pass
        
def mkIndex(all_shows,saveRoot,encoding='utf-8'):
  with io.open(saveRoot+"/"+"index.html", 'w+', encoding='utf-8') as f:
      with Encoded_File_Wrapper(f,encoding=encoding) as f2:
        writeHTMLHeader(f2)
        writeDN_Index_body(f2,all_shows,saveRoot)
        writeHTMLFooter(f2)   