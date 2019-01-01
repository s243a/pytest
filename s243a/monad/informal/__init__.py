#import s243a.monad.mdict
import inspect

def hprint(x):
    print('entering hprint')
    print(x)   
def hset(d,**kwords): #Not sure if I use this function
    for k,v in kwords:
        d[k]=v     
def hdo(*lines,**kw):
    args=kw.get('args',None), 
    d=kw.get('d',{})
    ops=kw.get('ops',None)
    out=args
    for i in range(0,len(lines)):
        line=lines[i]      
        out=assignKey(line, #typically ('var',fn) or fn. 'var' is a value to assign the output of fn
                      args=out, #the output of the last function which is the input to the next function
                      d=d, # a dictionary object used for assiging function results
                      ops=ops) # can be used to over-ride operations. Defualt operation is function compostion
    return out
def assignKey(line,     #typically ('var',fn) or fn. 'var' is a value to assign the output of fn
            args=None,  #the output of the last function which is the input to the next function
            d={},      # a dictionary object used for assiging function results
            ops=None): # can be used to over-ride operations. Defualt operation is function compostion
  out=args
  if isinstance(line,tuple) or \
     isinstance(line,list):
    if len(line)>1:
      if hasattr(line[1], '__call__'): #TODO and line[0] is string
        out=m_add_out_and_dict(line[1],args=out,d=d,ops=ops)
        d[line[0]]=out
        return line[1]
  elif hasattr(line,'__call__'):
    out=m_add_out_and_dict(line,args=out,d=d,ops=ops)
    return out
  raise ValueError('Bad input value or not yet implemented') #Maybe some other cases?
#dev
def add_out_and_dict(fn,args,d):
  spec=inspect.getargspec(fn)
  dict_i=-1
  for i in range(0,len(spec.args)):
      if spec.args[i]=='d':
        dict_i=i
        continue
      #We may add more to this loop
  if (len(spec)==1):
    if dict_i == -1:
        return lambda: fn(args)
    else:
        return lambda: fn(d)
  else:
      if dict_i==0:
        return lambda: fn(d,args)    
      elif dict_i==1:
        return lambda: fn(args,d)    
      else:
        return lambda: fn(args,d=d)      
      
def m_add_out_and_dict(fn,args,d={},ops=None):
  if ops is None: #This is 
    return add_out_and_dict(fn,args,d)
  else:
    if hasattr(ops,'op'):
      ops.op(args,fn)
    elif hasattr(ops,'bind'):
      ops.bind(args,fn)
    elif hasattr(ops,'next'):
      ops.next(args,fn)

out=hdo(   ('x', lambda d,o=[]: 1),              #x=1 and return x
           lambda d,o=[]: hprint(d['x']()),      #print previously returned value
           ('y', lambda d,o=[]: 2),              #y=2 and don't return anything (kind of like a let statment in Haskel)
           lambda d,o=[]: hprint(str(d['x']()+\
                                     d['y']())
                                )                #print previously assiigned x and y
       )
print("printing out")
print(out)
print("calling out")
out2=out()
print("printing out 2")
print(out2)