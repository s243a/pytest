from interface import implements, Interface

from freenet.store import freenet.store.StorableBlock
#Based on https://github.com/freenet/fred/blob/4e6bf4b0ea42b713a4261778fac9ca376dc28117/src/freenet/keys/KeyBlock.java
def KeyBlock(implements(StorableBlock)):
    def getKey():
        pass
    def getRawHeaders():
        pass
    def getPubkeyBytes():
        pass