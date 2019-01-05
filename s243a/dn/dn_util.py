import os,sys,re,pdb
PY2 = sys.version_info.major == 2
PY3 = sys.version_info.major == 3
def isString(obj):
    if PY3:
        string_types = str
    else:
        string_types = basestring
    if isinstance(obj,string_types):
        return True
    else:
        return False
def mkdir(path): #TODO move to s243a.util
    if not os.path.exists(str(path)):
        print("Making directory "+str(path))
        os.makedirs(str(path)) 
def parseURL(url,outKey=None):
    print("url="+url)
    #a_pattern=r'^(?P<protocol>[a-zA-Z]+)\:\/\/(?P<domain>[^/]+)(?P<path>\/.+)\/(?P<bname>[^/]*)$'
    a_pattern=r'^((?P<protocol>[a-zA-Z]*)\:\/\/(?P<domain>[^/]+))*(?P<path>\/?.+)\/(?P<bname>[^/]*)$'
    m=re.match(a_pattern,url)
    
    matches=m.groupdict()
    if outKey is None:
        return matches
    if isString(outKey):
        return matches[outKey]
    else:
        out=[]
        for key in outKey:
            out.append(matches[key])
        return tuple(out) #https://stackoverflow.com/questions/12836128/convert-list-to-tuple-in-python
#def getPath(url):
#    for arg in args
#       if hasattr(arg,'getPath')
#           return arg.getPath
#       elif isString(arg)
#           return parseURL(url)


def getAttrOrVal(item,key):
    if hasattr(item,key):
        return getattr(item,key)
    else:
        return item[key]
def getURLPart(url,*args,**defaults):
    #url=getAttrOrVal(show,html_attr)
    out=[]
    matches=None
    for arg in args:
        url_part=None
        if hasattr(url,'get_'+arg):                
            url_part=getattr(url,'get_'+arg)()
        elif isString(url):
            if matches is None:
                matches=parseURL(url)
            url_part=matches[arg]
        if url_part is None:
            if arg in defaults:
                url_part=defaults[arg]
        out.append(url_part)
        #if path[0]=="/":
        #path=path[1:]
    if len(out)>1:
        return tuple(out)
    else:
        return out[0]
def stripRoot(url,root):
    print("Stripping Root")
    print("url="+str(url))
    print("root="+str(root))
    #pdb.set_trace()
    part1=url[0:len(root)]
    if str(part1)==str(root):
        return url[len(root):]
    else:
        #pdb.set_trace()
        return url
def writeHTMLFooter(f):
    print('writeHTMLFooter')
    f.write("%s\n" % '</body>')        
    f.write("%s\n" % '</html>') 
def writeHTMLHeader(f):
    print('WriteHTMLHeader')
    f.write("%s\n" % '<!DOCTYPE html>')
    f.write("%s\n" % '<html>')
    f.write("%s\n" % '<body>')
def isiterable(p_object):
    try:
        it = iter(p_object)
    except TypeError: 
        return False
    return True
#https://stackoverflow.com/a/4668679/10866035
def itterator_or_None(obj):
    #print(str(obj))
    #pdb.set_trace()
    if isiterable(obj):
        return obj
    else:
        return [None]