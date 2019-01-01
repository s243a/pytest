import sgmllib, urllib, urlparse, os, pickle, md5, base64
import pdb, json #For debugging
#https://stackoverflow.com/questions/3031045/how-come-string-maketrans-does-not-work-in-python-3-1
from string import maketrans #Import might be slightly different in python 3
from s243a.fn import alt,seq0

#https://stackoverflow.com/questions/9698614/super-raises-typeerror-must-be-type-not-classobj-for-new-style-class
#https://stackoverflow.com/questions/9699591/instance-is-an-object-but-class-is-not-a-subclass-of-object-how-is-this-po/9699961#9699961

# https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples
bashEncoding={"\a",r"\a", # alert (bell)
              "\b",r"\b", # backspace

              "\f",r"\f", # form feed
              "\n",r"\n", # new line
              "\r",r"\r", # carriage return
              "\t",r"\t", # horizontal tab
              "\\",r"\\", # backslash
              "\'",r"\'", # single quote
              '\"',r'\"', # double quot#
              "?",r"\?"}  # question mark
def bashStrQuote(string,*unsafe):
    out=BashString([])
    for c in string:
        out.append(bashChrQuote(c,unsafe))
    return out
def bashChrQuote(char,*unsafe):
    if (len(unsafe)==0) or (char in unsafe):
        if char in bashEnconding:
            return bashEncoding[char]
        else:
            return char
    else:
        return char
#              "\v",r"\v", # vertical tab        
#              "\e",r"\e", #
#              "\E",r"\E"' # an escape character
#    \nnn   the eight-bit character whose value is the octal 
#           value nnn (one to three digits)
#    \xHH   the eight-bit character whose value is the hexadecimal
#           value HH (one or two hex digits)
#    \uHHHH the Unicode (ISO/IEC 10646) character whose value is 
#           the hexadecimal value HHHH (one to four hex digits)
#    \UHHHHHHHH the Unicode (ISO/IEC 10646) character whose value 
#               is the hexadecimal value HHHHHHHH (one to eight 
#               hex digits)
#    \cx    a control-x character
class BashString:
    def __init__(self,string):
        self.chars=[]
        for c in string:
            self.chars.append(string)
    def append(self,c):
        self.chars.append(c)
    def __str__(self):
        return ''.join(self.chars) #https://stackoverflow.com/questions/4435169/how-do-i-append-one-string-to-another-in-python
                
class SimplePathWatcher(object):
    def __init__(self,root):
        self.root=root
        self.raw_data=None
    def on_header(self,raw_data,obj=None,state=None):
        if state=="More":
            self.raw_data=self.raw_data+raw_data
        else:
            self.raw_data=raw_data
    def on_enter(self):
        pass
    def on_exit(self):
        pass
    def get_Dir():
        self.items[-1]['full']
class DictList(list):
    def __init__(self,*args):
        super(DictList,self).__init__(args)
    def append(self,**kw):
        super(DictList,self).append(kw)

intab = " _"
outtab = "_~"
transtab = maketrans(intab, outtab)

        
         
def setPathDefaults(obj):
        obj.sep='/'
        obj.MAX_PATH_LEN=200#typically is is 255 for the maxium path length in linux but we want to leave some room for the filename.
        obj.MAX_NESTING=0 #0 Means no limit on the amount of nexted directories.     
def getCallDel(kw,key,default,args):
    fn=kw.get(key,default)
    if fn is not None:
        return fn(args)
        del kw[key]
def setKwAttr(obj,kw):
    print(kw)
    #https://stackoverflow.com/questions/5466618/too-many-values-to-unpack-iterating-over-a-dict-key-string-value-list
    if hasattr(kw,'iteritems'): #Python 2 case
        itterator=lambda kw: kw.iteritems()
    else: #Python 3 case
        itterator=lambda kw: kw.items()
    print("kw="+str(kw))
    for k,v in itterator(kw):
        print("obj."+str(k)+"="+str(v))
        setattr(obj,k,v)
    #pdb.set_trace()
def hasherDefulats():
  return {\
    'hasher':    md5.md5(),
    'updateHash':lambda hasher,data: seq0(lambda: hasher.update("\n"),
                                          lambda: hasher.update(data)),
    'getDigest': lambda hasher: base64.b64encode(hasher.digest(),'~-')[0:22],
    'copyHash':  lambda hasher: hasher.copy()}
    #     
def setHashWrapper(obj,kw,delete=True):
    defaults=hasherDefulats()
    for key in ('hasher','updateHash','getDigest','copyHash'):
        val=kw.get(key,None)
        if val is not None:
            setattr(obj,key,val)
            if delete==True:
                del kw[key]
        else:
            setattr(obj,key,defaults[key])
class HashWrapper:
    def __init__(self,kw,delete=True):
        setHashWrapper(self,kw,delete=True)
    def update(self,data):
        return self.updateHash(self.hasher,data)
    def digest(self):
        return self.getDigest(self.hasher)
    def copy(self):
        kw={'hasher':self.copyHash(self.hasher),
            'updateHash':self.updateHash,
            'getDigest':self.getDigest,
            'copyHash':self.copyHash}
        return HashWrapper(kw)
class DictList_For_EncodedPathWatcher(DictList):
    def __init__(self,paths=[],**kw):
        super(DictList,self).__init__(paths)
        #setHasher(self)
        self.hasher=HashWrapper(kw,delete=True)
        if 'encoder' in kw.keys():
            self.encoder=kw['encoder']
        else:
            self.encoder=lambda raw_name: urllib.quote(raw_name.translate(transtab), safe='()?-,'+r"'"+r'"') #+"'"+'"'      
        #getCallDel(kw,'setHasher',setHasher,self)
        self.before_append=kw.get('before_append',lambda path: None)
        self.after_append=kw.get('after_append',lambda path: None)  
        self.before_pop=kw.get('before_pop',lambda path: None) 
        self.after_pop=kw.get('after_pop',lambda path: None)    
        self.root=kw.get('root',"/root/Downloads/pt")     

        getCallDel(kw,'setPathDefaults',setPathDefaults,self)

        setKwAttr(self,kw)       
        for path in paths:
            self.append(path)
    def append(self,raw_name,**kw):
        #alt(kw,'bname',self.updateBName(kw)) I think we need this
        if raw_name is not None:
            kw['raw_name']=raw_name   
        
        print("raw_name"+str(raw_name))

        alt(kw,'bname',lambda: self.encoder(kw['raw_name'])) 
        if len(self)>0:
            hasher=self[-1]['hasher'].copy()
            alt(kw,'hasher',lambda: hasher)        
            alt(kw,'nesting',lambda: self[-1]['nesting']+1)        
            alt(kw,'full',lambda: self[-1]['full']+self.sep+kw['bname'])
        else:
            hasher=self.hasher.copy()
            alt(kw,'hasher',lambda: hasher)        
            alt(kw,'nesting',lambda: 1)        
            alt(kw,'full',lambda: self.root+self.sep+kw['bname'])      
        #if kw['nesting']>1:
        folded=self.pathFold(kw)
        #else
        #    folded=False
        if len(self)>0:
            self.before_append(self[-1]['full'])
        else:
            pass #TODO, need to think about this
        super(DictList,self).append(kw)
        if folded:
            self.mkLinks()   
        self.after_append(self[-1]['full'])
    def rename(ind=-1,**kw):
        for key,value in kw:
            self[-1][key]=value
        #TODO, add logic for if one gives the bname here without the fullname or visa-versa
    def pop(self):
        last=self[-1]
        self.before_pop(last['full'],self) #No point in return a result.
        super(DictList,self).pop() 
        
        if len(self)>0:
            path=self[-1]['full']
            self.after_pop(path,last)   
        else: #This is probably pointless
            path=self.root
        
        #return result #I don't think this does anytning useful. 
    def getFullname():
        return self[-1].full                      
    def pathFold(self,kw):
        maxNesting=kw.get('maxNesting',self.MAX_NESTING) 
        root=kw.get('root',self.root)

        path=kw['full']
        pathlen=len(path)
        nesting=kw['nesting']
        if (nesting<=maxNesting or maxNesting==0) and \
           (pathlen<=self.MAX_PATH_LEN):
            return False #No Folding Required. 
        else:
            bname=kw['bname']
            hasher=kw['hasher']
            kw['bname']=bname+"-id"+hasher.digest()
            kw['full']=self.root+self.sep+'1'+self.sep+kw['bname'] #TODO give more options for the wrap folder
            return True
            #mkLinks=kw.get('mkLinks',self.mkLinks)
            #mkLinks(paths)  
    def mkLinks(self):#new_fullpath,last_fullpath):
           #dig=m.digest()
           #dig2=base64.b64encode(s,'~-') #Alt chacters are tilda and dash like in freenet: https://github.com/freenet/wiki/wiki/Signed-Subspace-Key
           #self.mkLinks(last.full,dig,dirname)
           
           new_fullpath = self[-1]['full']
           last_fullpath=self[-2]['full']
           bname=self[-1]['bname']
           sep=self.sep
           if not os.path.exists(new_fullpath):
             print("Making directory "+new_fullpath)
             os.makedirs(new_fullpath)
           #TODO Possible bug producting duplicate paths
           new_fullpath2=new_fullpath.replace("'",r"'\''")    #str(bashStrQuote(new_fullpath,"\'"))
           last_fullpath2=last_fullpath.replace("'",r"'\''")   #str(bashStrQuote(last_fullpath,"\'"))
           if not os.path.exists(new_fullpath+sep+"parent"):
             last_fullpath_rel=os.popen("realpath --relative-to='"+new_fullpath2+"' '"\
                                                                  +last_fullpath2+"'"\
                                       ).read().rstrip('\n')
             os.chdir(last_fullpath)    
             print("last_fullpath="+last_fullpath2)
             print("new_fullpath="+new_fullpath2)
             print("last_fullpath_rel"+last_fullpath_rel)          
             os.symlink(last_fullpath_rel,new_fullpath+sep+"parent")
           print(str(last_fullpath+sep+bname))
           if not os.path.exists(last_fullpath+sep+bname):
             last_fullpath2=last_fullpath.replace("'",r"'\''")  #str(bashStrQuote(last_fullpath,"\'"))
             new_fullpath2=new_fullpath.replace("'",r"'\''")    #str(bashStrQuote(new_fullpath,"\'"))  
             new_fullpath_rel=os.popen("realpath --relative-to='"+last_fullpath2+"' '"\
                                                                 +new_fullpath2+"'"\
                                      ).read().rstrip('\n') 
             os.chdir(new_fullpath)    
             os.symlink(new_fullpath_rel,last_fullpath+sep+bname)
           #paths.rename(-1,bname=bname,full=new_fullpath)   
#    def set_HashFn(hasher=None,updateHash=None,getDigest=None):
#        if hasher is not None: self.hasher=hasher
#        if updateHash is not None: self.updateHash=updateHash
#        if getDigest is not None: self.getDigest=getDigest
#        if copyHash is not None: self.copyHash=copyHash
#        return self


class EncodedPathWatcher(SimplePathWatcher):
    def __init__(self,root,**kw):
        #https://stackoverflow.com/questions/11179008/python-inheritance-typeerror-object-init-takes-no-parameters
        super(EncodedPathWatcher,self).__init__(root)    
        self.paths=DictList_For_EncodedPathWatcher([],**kw)
    def on_enter(self,raw_data=None,bname=None,items=None,obj=None):
        if raw_data is None:
            raw_data=self.raw_data
        self.paths.append(raw_data)
    #def mkLinks(self,last,dirname,m) 
  
    def on_exit(self):
        self.paths.pop()
    def encode(self,bname):
        return self.encoder(self.bname,self)
    def defaultEncoder(self,bname):
        return urllib.quote(self.bname, safe='()?-,'+r"'"+r'"') #+"'"+'"'
    #def defaultSymLast(
def storeList(path,obj):
        items=obj.items
        print('storeList')
        os.chdir(str(path))
        print(os.getcwd())
        pickle.dump(items,open( "list.p", "wb" )) 
        bname=os.path.basename(path)
        if bname in ():
            print(json.dumps(items,default=jdefault)) 
            print("store at "+str(path))
            pdb.set_trace()
        obj.items=[]
def mkdir(path):
    if not os.path.exists(str(path)):
        print("Making directory "+str(path))
        os.makedirs(str(path))   
#https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/        
def jdefault(o):
    return o.__dict__        
def loadList(path,obj):
    items=obj.items
    print('loadList')
    print('path='+str(path))
    os.chdir(str(path))
    print(str(path))
    print(os.getcwd())
    
    obj.items=pickle.load(open( "list.p", "rb" ))  
    print(json.dumps(items,default=jdefault))  
    #pdb.set_trace()
class HTML_Link:
    def __init__(self,**kw):
        self.text=kw.get("text"," ")
        self.href=kw.get("href",'/')
        self.add_date=kw.get("add_date",'0')
        self.linkType=kw.get("linkType",None)

    def toHTML(self,endSep=''):
        
        if self.linkType is None:
            str='<A HREF="'+self.href+'" ADD_DATE="'+self.add_date+'">'+self.text+"</A>"+endSep
            return str
        elif self.linkType.upper()=="FOLDER":
            str='<A HREF="'+self.href+'">'+self.text+"</A>"           
            return 'Folder: '+str+endSep
class Section:
    def __init__(self,text):
        self.text=text.replace('\n', ' ')
    def toHTML(self,endSep=''):
        return "<H3>"+self.text+"</H3><hr>"
def linkToLastHTML(obj,path,last,paths=None):
    if paths is not None:
        sep=paths.sep
    else:
        sep="/"
    items=obj.items
    last_path=last['full']
    #TODO improve security here and make the code more portable. 
    path2=path.replace("'",r"'\''") #bashStrQuote(path,"\'"))
    last_path2=last_path.replace("'",r"'\''")  #bashStrQuote(last_path,"\'"))
    href=urllib.quote(os.popen("realpath --relative-to='"+path2+"' '"\
                                                         +last_path2+"'"\
                              ).read().rstrip('\n'))
    href=href+sep+"index.html"
    print("href="+href)
    text=last['raw_name']
    linkType='FOLDER'
    items.append(HTML_Link(href=href,text=text,linkType=linkType))
    print(items[-1].toHTML())
    #pdb.set_trace()
class BookMarkParser(sgmllib.SGMLParser):
    def __init__(self,**kw):
        sgmllib.SGMLParser.__init__(self)
        self.STATE="__init__"
        self.items=[]
        self.watcher=kw.get('watcher',None) #This is the main watcher, we may add others

        if self.watcher is None:
            self.watcher=EncodedPathWatcher(root="/root/Downloads/pt",
                before_append=lambda path: storeList(path,self),
                after_append=lambda path: mkdir(path),
                before_pop=lambda path,paths: HTMLWriter(self,paths).writeList(path),
                after_pop=lambda path,last: \
                            seq0(lambda: loadList(path,self),
                                 lambda: linkToLastHTML(self,path,last)
                                )                
            )
            #self.watcher.enterCB=lambda dir: self.storeList(dir)
        self.watchers=[self.watcher]        
        

    def NotifyHeaderWatchers(self,data):
        for aWatcher in self.watchers:
            aWatcher.on_header(data,obj=self)

    def start_h3(self, attributes):
        print('start_H3')
        self.STATE='Started H3'
        for name, value in attributes:
            print(name+"="+value)
            if (value == 'FOLDED') or (name == 'folded'):
                self.STATE='FOLDED'
    def handle_data(self,data):
        print('handleData')
        print("self.STATE="+self.STATE)
        if self.STATE=='FOLDED':
            self.NotifyHeaderWatchers(data)

            #https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python

            self.STATE="Seeking DL"
 
        if self.STATE=="A":
            
            self.A.text=data
        if self.STATE=="DD":
            data2=data.split('\n')[0].strip()
            if len(data2)>0:
                self.items.append(Section(data2))
    def end_h3(self): #Probably redundant
        print('end_H3')
        self.FOLDED=False
    def start_dl(self, atributes):
        if self.STATE!="__init__":
            print('start_DL')
            for watcher in self.watchers:
                watcher.on_enter()   
            self.items=[]
    def end_dl(self):
        if self.STATE!="__init__":
            print('end_DL')
            for watcher in self.watchers:
                watcher.on_exit()          
    def start_a(self,atributes):
        if self.STATE!="__init__":
            print('start_A')
            self.A=HTML_Link()
            for key,value in atributes:
                setattr(self.A,key,value)
        self.STATE='A'
    def end_a(self):
        if self.STATE!="__init__":
            print('end_A')
            self.items.append(self.A)
            self.A=None
            self.STATE='Ended A'
    def do_dd(self, atributes):
        if self.STATE!="__init__":
            print('do_DD')
            self.STATE="DD"
    def do_dt(self, atributes):
        if self.STATE!="__init__":
            print('do_DT')
            self.STATE="DT"
class HTMLWriter:
    def __init__(self,obj,paths=None,maxParents=0):
        self.items=obj.items
        self.paths=paths
        self.maxParents=0
    def writeHTMLHeader(self,f):
        print('WriteHTMLHeader')
        f.write("%s\n" % '<!DOCTYPE html>')
        f.write("%s\n" % '<html>')
        f.write("%s\n" % '<body>')
    def writePath(self,f):
        f.write("<b>Reverse Path:</b> ")
        count=1
        paths=self.paths
        f.write('<a href=".">'+paths[-1]['bname']+"</a>"+" | ")
        href=".." 
        for i in range(len(paths)-2,-1,-1):
            f.write('<a href="'+href+'/index.html">'+paths[i]['bname']+"</a>") 
            count=count+1
            if (count>= self.maxParents) and (self.maxParents!=0):
                f.write("<br>")
                break
            else:
                href=href+"/.." #TODO make this more platform independent
                f.write(" |")
        f.write("<hr><br>")
    def writeHTMLFooter(self,f):
        print('writeHTMLFooter')
        f.write("%s\n" % '</body>')        
        f.write("%s\n" % '</html>')   
    def writeList(self,path):
        print('writeList')
        os.chdir(str(path))
        bname=os.path.basename(path)
        if bname in ():
            print("writeList "+bname)
            print(json.dumps(self.items,default=jdefault))  
            pdb.set_trace()
            debug_break=True
        else:
            debug_break=False
        with open('index.html', 'w') as f:
            self.writeHTMLHeader(f)
            self.writePath(f)
            for item in self.items:
                if item is not None:
                    out_str="%s\n" % item.toHTML('<br>')                        
                else:
                    out_str="<b>Empty Item!!!!</b>"
                f.write(out_str)
                if debug_break:
                    print("out_str="+out_str)
                    pdb.set_trace()
            self.writeHTMLFooter(f)        
        
