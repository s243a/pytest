import sys
PY2 = sys.version_info.major == 2
def itterate(kw,fn):
    itterator=getDictItterator(kw)
    for k,v in itterator(prefixes):
        r_prefixes[v]=k  
def getDictItteratorFn(obj):
    if hasattr(obj,'iteritems'): #Python 2 dictionary case
        itterator=lambda kw=obj: kw.iteritems()
    else: #Python 3 case
        itterator=lambda kw=obj: kw.items()    
    return itterator
def getDictItterator(obj):
    fn=getDictItteratorFn(obj)
    return fn(obj)