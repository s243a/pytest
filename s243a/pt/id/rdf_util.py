def setSchemaData(obj,clsSchema,*propertiesSchemas,**options):
    obj.schema=clsSchema
    setPropertySchemas(obj,*propertiesSchemas,**options):
    #itterator=getDictItterator(obj):
    #    for k,v in itterator:
    #        setattr(obj,k,v)
def setPropertySchemas(obj,*propertiesSchemas,**options):
    for property_schema in propertiesSchemas:
        set_aPropertySchema(obj,property_schema)
def set_aPropertySchema(obj,property_schema):
    prefix,localname=get_prefix_local_name(property_schema)
def get_prefix_local_name(a_schema):
    if hasattr(obj,'localname'):
        localname=obj.localname
    elif hasattr(obj,'qname'):
        try:
            prefix,localname=re.split
            return prefix,loclaname
        except:
            pass
    if localname is None
        if hasattr(obj,'rdfs_label'):
            localname=obj.label
    if hasattr(obj,'prefix'):
        prefix=obj.prefix
    if (localname is None) or (prefix is None)
      for prop in ('URI','rdf_about','rdfs_about') #TODO verify which is correct 'rdf_about' or 'rdfs_about' and put the correct one first
        if hasattr(obj,prop):
            tolkens=re.split(r'[/#]',URI)
            name_len=len(tolkens[-1])
            if name_len>0
                localname=tolkens[-1]
                ns=tolkens[:-name_len] #https://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string
                prefix=getPrefix(obj,ns)
                return prefix,localname
    #Assume we have a localname now.
    return getPrefix(obj,ns)
def getPrefix(**kw): #obj=None,ns=None,URI=None,about=None
    obj=kw.get('obj',None)
    URI=getFmFirst(obj,kw,default=None,
                   keys_or_attributes=('URI','rdf_about','rdfs_about'),
                   keys=('rdf:about,rdf:about')
    tolkens=re.split(r'[#/]',URI)
    ns=URI[:-len(tolkens[-1]]
    prefix=prefix_fm_namespace.get(ns,None)
    return prefix
def getFmFirst(*objects,**kw)
    for obj in objects:
        for attribute in keys_or_attributes
            if hasattr(object,'key'):
                return object.key
        if hasattr(object,'keys'):
            for key in join_collections(keys_or_attributes,keys)
               if key in object.keys():
                   return object[key]
def join_collections(*objects):
    out=[]
    for obj in objects
        for item in obj
           out.append(item)
def get_fm_kw_or_obj(kw,obj,key,default=None)
    if key in kw.keys():
        return kw.get(key)
    elif hasattr(obj,key):
        return obj.key