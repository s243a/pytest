alt_fn=lambda d,k,a: d.get(k,None) if d.get(k,None) is not None else a()
alt_fn_nc=lambda d,k,a: d.get(k,None) if d.get(k,None) is not None else a
def alt(d,k,a):
    d[k]=alt_fn(d,k,a)
def alt_nc(d,k,a):
    d[k]=alt_fn_nc(d,k,a)
def seq0(*args):
    for arg in args:
        arg()
iff_nc=lambda a,b,c: b if a else c
iff0=lambda a,b,c: b() if a else c()
iff_kw=lambda a,b,c,**kw: b(**kw) if a else c(**kw)
iff_args=lambda a,b,c,*args: b(**kw) if a else c(**kw)
iff=lambda a,b,c,*args,**kw: b(*args,**kw) if a else c(*args,**kw)
def lazyGet(kw,k,default=lambda: None): 
  return iff_nc(k in kw,
           lambda: kw.get(k),
           default) 
def safeCall(fn,*args,**kw):
    if callable(fn):
        print("Calling Object")
        return fn.__call__(*args,**kw)
    else:
        print("Object not callable")
        return fn