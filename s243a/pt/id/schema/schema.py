def setSchema(schemas)
  setProperty(properties,label="Literal";prefix="rdfs",subClassOf="rdfs:Resource",isDefinedBy="<http://www.w3.org/2000/01/rdf-schema#>")
schemas_by_prefix
schemas_by_uri
def getFirstFmDict(kw,*args,default=Nothing): #'localname','label'
    for arg in args:
        if key in by_uri:
            return by_uri[arg]
        return default
class Schema_Container:
    by_prefix=None
    by_ns=None
    by_uri={}
    by_qname={}
    prefix_by_ns={}
    namespace_by_prefix={}
    def __init__(self,**kw):
       this.by_prefix=kw.get('by_prefix',type(self).by_prefix) 
       this.get_byPrefix=kw.get('get_byPrefix',
           lambda *args,default=Nothing: getFirstFmDict(self.by_prefix,*args,default))        
       
       this.by_ns=kw.get('by_ns',type(self).by_ns) 
       this.get_byNS=kw.get('get_byNS',
           lambda *args,default=Nothing: getFirstFmDict(self.by_ns,*args,default))  
       
       this.by_uri=kw.get('by_uri',type(self).by_uri)
       this.get_byURI=kw.get('get_byURI',
           lambda *args,default=Nothing: getFirstFmDict(self.by_uri,*args,default))     
             
       this.by_qname=kw.get('by_qname',type(self).by_qname)
       this.get_byQName=kw.get('get_byQName', 
           lambda *args,default=Nothing: getFirstFmDict(self.by_qname,*args,default))    
              
       this.prefix_by_ns=kw.get('prefix_by_ns',type(self).prefix_by_ns
       this.get_PrefixByNS=kw.get('get_PrefixByNS', 
           lambda *args,default=Nothing: getFirstFmDict(self.prefix_by_ns,*args,default)) 

       this.namespace_by_prefix=kw.get('namespace_by_prefix',type(self).prefix_by_ns
       this.get_namespaceByPrefix=kw.get('get_namespaceByPrefix', 
           lambda *args,default=Nothing: getFirstFmDict(self.namespace_by_prefix,*args,default)) 
    def append(self,a_schema):
        #getFmFirst((a_schema),keys_or_attributes=('URI','rdf_about','rdfs_about'))
        (prefix,uri,localname)=a_schema.__getitems__('prefix','uri','localname')
        self.add_by_prefix(prefix,schema)
    def cls_getItem(**kw)
        localname=self.getFirst(kw,'localname','Label')
        if localname is not None
            uri=getURI_fm_FN('URI','name')
            ns,localname=parse_ns_localname(uri)
            
default_schema_container=Schema_Container()
def mk_Schema(parent,cls,**kw)
    cls.__N
class Schema(object):
    def __init__(parent,**kw):
        if 'default_schema_container' in globals():
            self.schema_container=default_schema_container
        else
            self.schema_container=None
        self.props=[]
        itterate(kw,lambda k,v:setattr(self.props,key,value))
        self.childern=[]
        self.cls=[] #The class object associated with the schema
        self.objects=[] #Instances
        self.properties=[]
    def getLocalName():
        if hasattr('localname'):
            return self.localname
        elif hasattr('qname'):
            (prefix,localname)=self.qname.split(":")
            self.localname=localname
            return self.localname
        elif hasattr('URI'):
            tolkens=re.split(r'[#/]',URI)
            return tolkens[-1]
        elif hasattr('rdfs_label'):
            return self.rdfs_label
    def getPrefix():
        if hasattr(self,'prefix'):
            return self.prefix
        elif hasattr('qname'):
            (prefix,localname)=self.qname.split(":")
            self.prefix=prefix
            return prefix
    def getURI():
        if hasattr(self,'URI'):
            return self.URI
        if hasattr(self,'ns'):
            ns=self.ns
        elif hasattr(self,'prefix') and (self.schema_container is not None):
            prefix=self.prefix
            ns=self.schema_container.get_namespaceByPrefix(prefix)
        elif hasattr(self,'rdfs_isDefinedBy'):
            patten=r'^[<](?P<url>.*[>]$'
        #elif hasattr('URI'):
        #    re.split(r'[/#]',self.URI) #Commented out untill I fix this
        #elif
        #elif hasattr('rdf:about')
        #elif hasattr('rdfs_isDefinedBy') #Probably not workable

rdfs_Class=
  Schema(None,
    a="rdfs_Class",prefix=rdfs,
    URI="http://www.w3.org/2000/01/rdf-schema#"+"Class"
    ns="http://www.w3.org/2000/01/rdf-schema#"
    qname="rdfs:Class"
    rdfs_isDefinedBy="<http://www.w3.org/2000/01/rdf-schema#>",
    rdfs_label="Class",
    rdfs_comment="The class of classes.",
    rdfs_subClassOf="rdfs:Resource") 
class Class:y
    def __init__():
        self.schema=rdfs_Class        
rdfs_Resource= 
  Schema(RDFS_Class_Schema,     
    a="rdfs:Class",prefix=rdfs,
    URI='http://www.w3.org/2000/01/rdf-schema#'+'Resource',
    ns="http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    qname="rdfs:Resource"
    rdfs_isDefinedBy="<http://www.w3.org/2000/01/rdf-schema#>",
    rdfs_label="Resource",
    rdfs_comment="The class resource, everything.")
class Resource(Class):
    def __init__(uri)
       self.schema=rdfs_Resource
       self.URI=uri   
rdfs_Property=\
  Schema(rdfs_Class,
    a='rdfs:Class',prefix="rdfs"
    URI="http://www.w3.org/1999/02/22-rdf-syntax-ns#"+Property
    NS="http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    qname="rdfs:Property",
    rdfs_isDefinedBy="<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
    rdfs_label="Property",
    rdfs_comment="The class of RDF properties.",
    rdfs_subClassOf="rdfs:Resource")
#https://www.facebook.com/groups/TheSemanticWeb/permalink/10157987389396729/
rdf_Property=rdfs_Property.copy() #TODO verify that this works as intended
rdf_Property.qname="rdf:Property"
rdf_Property.prefix="rdfs"
dcterms_title=\
  Schema(rdfs_Property,  
    a="rdf:Property",  
    ns="http://purl.org/dc/elements/1.1/title",
    URI="http://purl.org/dc/elements/1.1/"+title,
    prefix="dcterms",
    qname="dcterms_Title",
    dcterms_hasVersion="<http://dublincore.org/usage/terms/history/#title-006>":,
    dcterms_issued='"1999-07-02"^^<http://www.w3.org/2001/XMLSchema#date>',
    dcterms_modified='"2008-01-14"^^<http://www.w3.org/2001/XMLSchema#date>',
    rdfs_comment="A name given to the resource."#@en,
    rdfs_isDefinedBy="<http://purl.org/dc/elements/1.1/>",
    rdfs_label="Title"#@en',
    skos_note="A second property with the same name as this property has been declared in the dcterms: namespace (http://purl.org/dc/terms/).  See the Introduction to the document \"DCMI Metadata Terms\" (http://dublincore.org/documents/dcmi-terms/) for an explanation.")#@en
dcterms_date=\
  Schema(rdfs_Property
    a="rdfs:Property"
    URI="http://purl.org/dc/elements/1.1/date"
    ns="http://purl.org/dc/elements/1.1/"
    dcterms_description="Date may be used to express temporal information at any level of granularity.  Recommended best practice is to use an encoding scheme, such as the W3CDTF profile of ISO 8601 [W3CDTF].",#@en ;
    dcterms_hasVersion="<http://dublincore.org/usage/terms/history/#date-006>",
    dcterms_issued="1999-07-02" #^^<http://www.w3.org/2001/XMLSchema#date>',
    dcterms_modified="2008-01-14" #^^<http://www.w3.org/2001/XMLSchema#date> ;
    rdfs_comment="A point or period of time associated with an event in the lifecycle of the resource." #@en ;
    rdfs_isDefinedBy="<http://purl.org/dc/elements/1.1/>" ;
    rdfs_label="Date"@en ;
    skos_note="A second property with the same name as this property has been declared in the dcterms: namespace (http://purl.org/dc/terms/).  See the Introduction to the document \"DCMI Metadata Terms\" (http://dublincore.org/documents/dcmi-terms/) for an explanation." #@en .
pt_rootTree=\
  Schema(rdfs_Property,a="rdfs:Property",
    rdf_about="http://www.pearltrees.com/rdf/0.1/#rootTree",
    rdfs_domain=Resource("http://xmlns.com/foaf/0.1/OnlineAccount"),
    rdfs_range=Resource=("http://www.pearltrees.com/rdf/0.1/#Tree"))
pt_treeId=\
  Schema(rdfs_Property,a="rdfs:Property",    
    rdf_about="http://www.pearltrees.com/rdf/0.1/#treeId",
    rdfs_comment="Tree identifier in pearltrees database.",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Tree"),
    rdfs_range=Resource("http://www.w3.org/2000/01/rdf-schema#Literal"))
pt_assoId=\
  Schema(rdfs_Property,a="rdfs:Property",
    rdf_about="http://www.pearltrees.com/rdf/0.1/#assoId",
    rdfs_comment="Trees belong to associations (group of trees).",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Tree"),
    rdfs_range=Resource("http://www.w3.org/2000/01/rdf-schema#Literal"))
pt_lastUpdate=
  Schema(rdfs_Property,a="rdfs:Property",
    rdf_about="http://www.pearltrees.com/rdf/0.1/#lastUpdate",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Tree"),
    rdfs_subPropertyOf=Resource("http://purl.org/dc/elements/1.1/date"))
inTreeSinceDate=\   
  Schema(rdfs_Property,
    a="rdfs:Property",
    rdf_about="http://www.pearltrees.com/rdf/0.1/#inTreeSinceDate",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Pearl"),
    rdfs_subPropertyOf=Resource("http://purl.org/dc/elements/1.1/date"))
    
pt_parentTree=\
  Schema=(rdf_syntax_ns_Property,
    a="rdf:Property",  
    localname="parentTree",
    ns="http://www.pearltrees.com/rdf/0.1/#",
    URI="http://www.pearltrees.com/rdf/0.1/#parentTree",
    prefix="pt",
    qname="pt:parentTree"
    rdf_about="http://www.pearltrees.com/rdf/0.1/#parentTree",
    rdf_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Pearl"),
    rdf_range=Resource("http://www.pearltrees.com/rdf/0.1/#Tree"))
pt_leftPos=\
  Schema(rdf_syntax_ns_Property,
   a="rdfs:Property",
   localname="leftPos",
   ns="http://www.pearltrees.com/rdf/0.1/#",
   qname="pt:leftPos",
   URI="http://www.pearltrees.com/rdf/0.1/#leftPos",
   rdf_about="http://www.pearltrees.com/rdf/0.1/#leftPos",
   rdfs_comment="see: http://en.wikipedia.org/wiki/Nested_set_model",
   rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Pearl")
   rdfs_range=Resource("http://www.w3.org/2000/01/rdf-schema#Literal"))
pt_rightPos=\
  Schema(rdf_syntax_ns_Property,a="rdfs:Property",
   localname="leftPos",qname="pt:rightPos",   
   ns="http://www.pearltrees.com/rdf/0.1/#",
   rdf_about="http://www.pearltrees.com/rdf/0.1/#rightPos",
   rdfs_comment="see: http://en.wikipedia.org/wiki/Nested_set_model",
   rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Pearl"),
   rdfs_range=Resource("http://www.w3.org/2000/01/rdf-schema#Literal"))
pt_noteText=\ 
  Schema(rdf_syntax_ns_Property,a="rdfs:Property",
    localname="noteText",qname="pt:noteText",  
    rdf_about="http://www.pearltrees.com/rdf/0.1/#noteText",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Note"),
    rdfs_range=Resource("http://www.w3.org/2000/01/rdf-schema#Literal"))
pt_parentPearl=\
  Schema(rdf_syntax_ns_Property,a="rdfs:Property",    
    rdf_about="http://www.pearltrees.com/rdf/0.1/#parentPearl",
    rdfs_domain=Resource("http://www.pearltrees.com/rdf/0.1/#Note"),
    rdfs_range=Resource("http://www.pearltrees.com/rdf/0.1/#Pearl"))

    