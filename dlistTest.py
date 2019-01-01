class DictList(list):
    def __init__(self,*args):
        super(DictList,self).__init__(args)
    def append(self,**kw):
        super(DictList,self).append(kw)
        
dl=DictList(1,2)
dl.append(a=3)
print(dl[-1]['a'])         
print(dl[-2]) 
        
