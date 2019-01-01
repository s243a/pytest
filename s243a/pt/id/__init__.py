import s243a.util
import s243a.pt.id.schema
import s243a.pt.id.rdf_util
class RDFS_Class(object):
  about='http://www.w3.org/2000/01/rdf-schema#Class' 
  prefix='rdfs'
  schema=schemas_by_prefix['rdfs:Class']
  propSchema=self.schema.properties
  def __init__(**kw)
      self.properties={}
      itterate(self.properties,lambda k,v:setattr(self,k,v))
      self.schema.cls=self
  def get_prefix(self):
      if hasattr(self,'prefix'):
          return self.prefix
      else
         return type(self).prefix      
  def get_about(self):
      if hasattr(self,'about'):
          return self.about
      else
         return type(self).about
  def __access_schema(self):
       if hasattr(self,'schema'):
          return self.schema
      else
          return type(self).schema   
  def get_schema(self):
      self.__access_schema.copy()

  def get_qname(self,sep=":"):
      return self.get_prefix()+sep+self.get_localname()
  def get_label(self):
      return self.__access_schema.label
  def get_localname(self):
      if not (hasattr(self,localname) and (self.localname is not None)):
         schema=self.__access_schema() 
         self.localname=type(self).cls_localname(schema)
      return self.localname
  @staticmethod      
  def cls_localname(schema=None):
      if schema is None:
          schema=RDFS_Class.schema
      if not hasattr(RDFS_Class,localname):
          RDFS_Class.localname=\
            getFmFirst(schema,default=None,
                       keys_or_attributes=('localname','rdfs_label','rdf_label'),
                       keys=('rdfs:label','rdf:label')
      if RDFS_Class.localname is None:
          prefix,localname=get_prefix_local_name(schema)
          RDFS_Class.localname=localname
          if RDFS_Class.prefix is None:
              RDFS_Class.prefix=prefix
      return RDFS_Class.localname
  def get_prefix(self):
      if hasattr(self,prefix) and (self.prefix is not None):
          return self.prefix
      else
          self.prefix=type(self).cls_prefix()
      return self.prefix
  @staticmethod
  def cls_prefix(schema=None):
      if schema is None:
          schema=RDFS_Class.schema
      if not hasattr(RDFS_Class,prefix):
          RDFS_Class.prefix=getPrefix(schema)
      return RDFS_Class.prefix
class PT_Item(RDFS_Class):
    
    def __init__(**kw):
        self.title=rtnFirstAndDel(kw,('dcterms_title','title'),"")
        super(pt_Tree,self).__init__(**kw) #TODO verify that it is okay to not have super as the first statment
        self.props['dcterms_title']=self.title
class PT_Tree(pt_Item):
    classSchema=Nothing
    propSchema={}
    def __init__(**kw):
      rorder=kw.get('r_order',False)
      if r_order==False:  
        self.creator=rtnFirstAndDel(kw,('dcterms_creator','creator','dcterms:creator'),"")
        self.treeId=rtnFirstAndDel(kw,('pt_treeId','treeId','pt:treeId'),None)
        self.assoId=rtnFirstAndDel(kw,('pt_assoId','assoId','pt:assoId'),None)
        self.lastUpdate=rtnFirstAndDel(kw,('pt_lastUpdate','lastUpdate','pt:lastUpdate'),None)
        self.privacy=rtnFirstAndDel(kw,('pt_privacy','privacy''pt_privacy'),0)
      else:
        self.creator=rtnFirstAndDel(kw,('dcterms:creator','creator','dcterms_creator'),"")
        self.treeId=rtnFirstAndDel(kw,('pt:treeId','treeId','pt_treeId'),None)
        self.assoId=rtnFirstAndDel(kw,('pt:assoId','assoId','pt_assoId'),None)
        self.lastUpdate=rtnFirstAndDel(kw,('pt:lastUpdate','lastUpdate','pt_lastUpdate'),None)
        self.privacy=rtnFirstAndDel(kw,('pt:privacy','privacy''pt_privacy'),0)        
      super(pt_Tree,self).__init__(**kw) #TODO verify that it is okay to not have super as the first statment
      self.props['dcterms_creator']=self.creator
      self.props['pt_treeID']=self.treeID
      self.props['pt_assoId']=self.assoId
      self.props['pt_lastUpdate']=self.lastUpdate
      self.props['pt_privacy']=self.privacy
PT_Tree.classSchema=
class PT_Pearl(pt_Item):
    def __init__(**kw):   
      rorder=kw.get('r_order',False)
      if r_order==False:  
        self.parentTree=rtnFirstAndDel(kw,('pt_parentTree','parentTree','pt:parentTree','),None)
        self.inTreeSinceDate=rtnFirstAndDel(kw,('pt_inTreeSinceDate','inTreeSinceDate','pt:inTreeSinceDate'),None)
        self.leftPos=rtnFirstAndDel(kw,('pt_leftPos','leftPos','pt:leftPos'),None)
        self.rightPos=rtnFirstAndDel(kw,('pt_rightPos','rightPos','pt:rightPos'),0)
        self.identifier=rtnFirstAndDel(kw,('dcterms_identifier','identifier','dcterms:identifier'),None)
      else
        self.parentTree=rtnFirstAndDel(kw,('pt:parentTree','parentTree','pt_parentTree','),None)
        self.inTreeSinceDate=rtnFirstAndDel(kw,('pt:inTreeSinceDate','inTreeSinceDate','pt_inTreeSinceDate'),None)
        self.leftPos=rtnFirstAndDel(kw,('pt:leftPos','leftPos','pt_leftPos'),None)
        self.rightPos=rtnFirstAndDel(kw,('pt:rightPos','rightPos','pt_rightPos'),0)
        self.identifier=rtnFirstAndDel(kw,('dcterms:identifier','identifier','dcterms_identifier'),None)
        
      super(pt_Tree,self).__init__(**kw) #TODO verify that it is okay to not have super as the first statment
      self.props['pt:parentTree']=self.parentTree
      self.props['pt:inTreeSinceDate']=self.inTreeSinceDate
      self.props['pt:leftPos']=self.leftPos
      self.props['pt:rightPos']=self.rightPos
      self.props['dcterms:identifier']=self.rightPos       
class PT_Page(PT_Pearl):
    def __init__(**kw)
        self.identifier=rtnFirstAndDel(kw,('dcterms_identifier,'identifier'),None)
        super(pt_Page,self).__init__(**kw) #TODO verify that it is okay to not have super as the first statment          
        self.props['dcterms_identifier']=self.parentTree



