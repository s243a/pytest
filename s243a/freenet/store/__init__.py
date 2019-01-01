#Based on https://github.com/freenet/fred/blob/4e6bf4b0ea42b713a4261778fac9ca376dc28117/src/freenet/store/StorableBlock.java
from interface import implements, Interface
class StorableBlock(Interface):
    getRoutingKey(Interface)
        pass #Should return byte array or list
    getFullKey()
        pass #Should return byte array or list