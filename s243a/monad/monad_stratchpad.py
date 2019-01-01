# Infix class by Ferdinand Jamitzky


from interface import implements, Interface
lambda rcompose fn1,fn2: fn2(fn1) 
bindAply = lambda action1 action2: compose(action1(),lambda x: action2(x))
pupURI=labmda: out.node.put(uri, nessage, mimetype=kw.mimetype, verbosity=kw.verbosity)
setJobOrCB=lambda x: iff(async=true,kw.startCB=x,kw.job= x())
rcompose(putURI,                             #if async returns callback, else returns job
         setJobOrCB) #x is the result of put URI
iff(async==True,kw['k1']=y,kw['k2']=y
ifNone(a,b) = a if a is None else b
def mReturn(fn):
    return lambda x: [x]+[fn(x)]
def doBind(call=lambda f: f(),bind=bindAply,rtn=mReturn,monad=None,*fns):
    if monad is not None:
        call=ifNone(call,monad.__call__)
        bind=ifNone(bind,monad.mbind)
        rtn=ifNone(rtn,monad.mreturn)
    vars=[]
    out=fns(i)
    for i in range(1,len(fns)):
        bind(fns(i),lambda x: rtn(call(fins(i+1,))
dev evalDo(out,out2):
    if isinstance(out2,list):
        
def mDo(**lines):
    out={}
    for x,v in lines:
        out['k']=v
    out2=out['rtn']
class Infix:
  def __init__(self, function):
      self.function = function
  def __ror__(self, other):
      return Infix(lambda x, self=self, other=other: self.function(other, x))
  def __or__(self, other):
      return self.function(other)
  def __call__(self, value1, value2):
      return self.function(value1, value2)
def mbind(m,fn):
    return Infix(lambda m: fn(m))
def state_bind(m,fn):
    return Infix(lambda m, fn: fn(m.a))
def state_return(fn):
    return     
def dict_state_bind(m,fn): #fn should return a monad
    return Infix(lambda: m, fn:fn(m.a,m.args)
def dict_state_retun(a):    
    return lambda: lamda a:->Dict_State(a=a) #x
def stae_mzero(m,fn):
    return State()
class State:
    __init__(a=None):
        self.a=a
    def mbind(self,fn):
        return state_bind(self,fn)

class Dict_State(State)
    __init__(args={},a=None,state=None)
        if a is not None:
            super().__init__(a)
        elif state is not None:
            super().__init__(state.a)
        self.args=args #d is a dictonary
    def mbind(self,fn)
        dict_state_bind(self,fn)
        
class monad(bind=dict_Bind):
    def mbind(self,b)
        pass
    def rev_mbind        
        