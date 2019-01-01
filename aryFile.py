#__getitem__(self, key) Defines behavior for when an item is accessed, using the notation self[key].
# This is also part of both the mutable and immutable container protocols. It should also raise
#  appropriate exceptions: TypeError if the type of the key is wrong and KeyError if there is no
#   corresponding value for the key.
# __setitem__(self, key, value) Defines behavior for when an item is assigned to, using the notation
#  self[nkey] = value. This is part of the mutable container protocol. Again, you should raise KeyError 
#  and TypeError where appropriate. 

class ArrayFile:
    __init__(self,obj=None,bitChunk=8,byteChunk=0)
    self.ary=ary
    self.strm=strm
    self.getCB=None
    self.setCB=None
    self.fp=None
    if isinstance(obj, list):
        self.getCB=lambda key: obj[key] #To make this safer we might want to turn lists into byte arrays
        self.setCB=lambda key, val: obj[key]=val
#https://stackoverflow.com/questions/1661262/check-if-object-is-file-like-in-python
    elif isinstance(obj, file) or
         isinstance(obj, io.IOBase) or
         isinstance(obj, io.TextIOBase) or
         isinstance(obj, io.BufferedIOBase) or
         isinstance(obj, io.RawIOBase) or
         isinstance(obj, io.IOBase):
        self.fp=obj
        if byteChunk!=0:
            bitCunk=byteChunk*8
            rBit=0
        else:
            bitChunk = int(byteChunk/8)
            rBit=int(byteChunk%8) 
        #https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python    
        #textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
        #is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        if rBit==0:
            self.getCB=self.fileByteSeekGet
            self.setCB=self.fileByteSeekSet
        else: #Not yet Implemented
            self.getCB=self.seekgetCBAwk
            self.setCB=self.setCBAwk           
    def fileByteSeekGet(self,byteKey):
        self.fp.seek(byteKey)
        return self.fp.read(self,self.byteChunk)
    def fileByteSeekSet(self,key,value)
        self.fp.seek(key)
        self.fp.write(value)=value //Will this write more than one byte?
    def fileBitSeekGet(self,bitKey): 
        bytSeek=int(bitKey/8)
        rBitSeek1=
        rBitSeek2=
        keep1,keep2,set1,set2=getMasks(bitKey,byteChunk)

        return self.fp.read(self.byteChunk)
        pass #Not yet implemented
    def fileBitSeekGetSet(self,key,value)
        #self.fp.seek(key)
        #self.fp.write(value)        
        pass #Not yet implemented