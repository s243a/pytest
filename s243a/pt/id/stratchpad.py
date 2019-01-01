import urllib
import sys
import s243a.pt.id.schema
PY2 = sys.version_info.major == 2
from s243a.fn import alt,seq0
prefixes={}
r_prefixes={}
schemas={}
properties={}
      
def rtnFirst(kw,options,default=None)
   for key in options
       if key in kw:
           return kw[key]
   return default 
def rtnFirstAndDel(kw,options,default=None)
   for key in options
       if key in kw:
           val=kw[key]
           del kw[key]
           return val
   return default 

def properties(properties)
    setProperty(properties,domain="pt:Tree",range="dcterms:Title",range='rdfs:Literal')
def update_schema(cls):
    cls.schema.cls=cls

update_schema(RDFS_Class)
def setPrefixes(prefixes)
    alt(prefixes,'pt','http://www.pearltrees.com/rdf/0.1/#')
    alt(prefixes,'rdf',"http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    alt(prefixes,rdfs="http://www.w3.org/2000/01/rdf-schema#")
    alt(prefixes,foaf="http://xmlns.com/foaf/0.1/")
    alt(prefixes,dcterms="http://purl.org/dc/elements/1.1/")
    if hasattr(props,'iteritems'): #Python 2 dictionary case
        itterator=lambda kw: kw.iteritems()
    else: #Python 3 case
        itterator=lambda kw: kw.items()
    for k,v in itterator(prefixes):
        r_prefixes[v]=k
    return r_prefixes #There are probably better semantics for this. 
r_prefixes=r_prefixes


#  @static
#  def get_attr_name(key,sep1="_",sep2="_"): #Split on sep1 combine with sep2
#      (prefix,localname,sucess)=parse_prefix_label(key,sep1)
#      if sucess:
#          return prefix+sep2+localname
#      else
#          for prop in get_propItterator:
#              (prefix2,localname2,sucess)=parse_prefix_label(key,sep1)
#              if sucess:
#                  if localname==localname2:
#                      return prefix2+sep2*localname
#def set_if_not_None(obj,key,value):
#    if key is not None:
#        setattr(obj,key,value)
def parse_prefix_label(key,sep="_")
  tolkens=re.split('[-:]', k)
  if len(tokens>2):
    return (None,k,False) #Failed
  elif len(tolkens)=1
    return (None,result[0],True)
  if len(tolkens)=2:
    (prefix,localname,True)
def parseRDF_Item(k,v=None): #We might not need the key
    if isStr(k):
        tolkens=re.split('[-:]', k)
        if len(tokens>2):
            return (None,k,False) #Failed
        elif len(tolkens)=1
            return (None,result[0],True)
        if len(tolkens)=2:
            (uri,Sucess)=getURI(tolkens[0]) #Teturns tokens[0] for uri if uri lookup fails
            return (uri,tolkens[1],sucess)
    elif instanceof(k,RDF_Property)
       uri=k.about
       if uri in r_prefixes:
           prefix=r_prefixes[uri]
       else:
           prefix=None
class RDFS_Resource(RDFS_Class):
  #def __init__(self):
  #self(RDFS_Resource,self).__init__()
  self.about='http://www.w3.org/2000/01/rdf-schema#Resource' 
  self.schema=Schema(a=self.schema=Schema(a="rdfs:Resource",
    rdfs_isDefinedBy="<http://www.w3.org/2000/01/rdf-schema#>",
    rdfs_label      ="Class",
    rdfs_comment    ="The class of classes.",
    rdfs_subClassOf ="rdfs:Resource")
class RDFS_Property(RDFS_Class):
  #self(RDFS_Resource,self).__init__()
  self.about='http://www.w3.org/2000/01/rdf-schema#Property'
  self.schema=Schema(a=self.schema=Schema(a="rdfs:Resource",      
    rdfs_subClassOf ="rdf:Property",
    rdfs_isDefinedBy="<http://www.w3.org/2000/01/rdf-schema#>",
    rdfs_label      ="subClassOf",
    rdfs_comment    ="The subject is a subclass of a class.",
    rdfs_range      ="rdfs:Class",
    rdfs_domain     ="rdfs:Class")
    self.value=value
  def __init__(**kw)
     self.val=kw.get('val') #Will fail if 'val' doesn't exit
     self.obj=kw.get('obj',None)
  def getDomain(self):
    if hasattr(self,'rdfs_domain'):
        return rdfs_domain
    else
        return self.__access_schema().rdfs_domain
  def getObj(self)
     return self.obj
  def getVal(self)
     return self.val
  #Maybe rdfs:Literal as default.
    def __init__(val,**kw):
#class PtItem:
#    def __init__(**kw)
#        super(PtFolder,self).__init(kw)
#        self.getTitle=self.properites['title']
#        self.inTreeSinceDate=self.properties['inTreeSinceDate'] 
#        self.attributes=kw   
#        self.text=kw.get('URI',text)       
#        self.date_created  
#    def getTitle():
#        if 
#class PtFolder(PtItem):
#    def __init__(**kw):
#        super(PtFolder,self).__init(kw)
#        self.items=kw.get('items',[])
#        self.parents=kw.get('parents',None)
#        if self.parents is None:
#            self.parents=[]
#            if parent in kw:
#                self.parents.append(kw['parent']) #The first item is the imediate parent. 
class PT_Tree(PtFolder):   
    def __init__(**kw)
        self.getAbout=lambda: self.URI
        self.getIdentifier=lambda: self.URI
        self.getTitle=lambda: self.title
        self.getParentTree=lambda: self.parents[0]
        self.getInTreeSinceDate=lambda: self.date_created
class PearlPage(                

#class RDF_Class(RDF_Item)
#  def __init__(**kw):
#
#    props=kw.get('properties',None) #A dictionary
#    self.props={}
#    if props is not None:
#      if hasattr(props,'iteritems'): #Python 2 dictionary case
#        itterator=lambda props: props.iteritems()
#      else: #Python 3 case
#        itterator=lambda props: props.items()
#      for k,v in itterator(props):
#        (uri,prefix,localname,sucess)=parseRDF_Item(k)
#        self.setProp(v,localname,uri=uri,prefix=prefix)
#    def getProp(lself,localname,prefix="",uri="")
#      return f_1stkey(self.props,
#                       (uri+'\n'+localname,lambda x: x),
#                       (prefix+'\n'localname,lambda x:x()),
#                       (localname,lambda x:x())
#                     )
#    def setProp(self,value,localname,uri=None,prefix=None):
#        if uri is Not None
#            self.props[uri+'\n'+localname]=value
#            self.props[prefix+'\n'+localname]=lambda: self.props[uri+'\n'+localname]            
#            self.props[localname]=lambda: self.props[uri+'\n'+localname]
#        elif prefix is Not None
#            self.props[prefix+'\n'+localname]=lambda: value        
#            self.props[localname]=lambda: self.props[prefix+'\n'+localname]()
#        else
#            self.props[localname]=lambda:value

def f_1stkey(d,*args):
    for arg in args #arg=(key,fn)
        if arg[0] in d:
            fn=arg[1]
            x=d[arg[0]]
            return fn(x)
    #TODO thow an exception if we haven't returned a value.


def getURI(prefix_or_uri):
    if prefix_or_uri in prefixes:
        return (prefixes[prefix_or_uri],True)
    elif prefix_or_uri in r_prefixes:
        return (prefix_or_uri,True)
    else
        return (prefix_or_uri,False) #Unknown URI
def isStr(string):
  # Check if string (lenient for byte-strings on Py2):
  isinstance(string, basestring if PY2 else str)
  # Check if strictly a string (unicode-string):
  isinstance(string, unicode if PY2 else str)
   
  #What is this for?
  #https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
  ## Check if either string (unicode-string) or byte-string:
  #isinstance('abc', basestring if PY2 else (str, bytes))
  
  #Is a bytestring really a string?
  #https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
  ## Check for byte-string (Py3 and Py2.7):
  #isinstance('abc', bytes)

    