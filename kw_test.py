from s243a.util import *
def test(**kw):
    itterator=getDictItterator(kw)
    for k,v in itterator:
        print(k+"="+str(v))
#test(**{'a:b':1})
from xml.sax.handler import ContentHandler
from s243a.pt.id.schema import *
class MyContentHandler(ContentHandler):
    trees={}
    pearls={}
    def __init__(self,**kw):
        self.trees=kw.get(trees,{})
        self.pearls=kw.get(pearls,{})
        self.subject=None
        self.type=None
    def startElementNS(self, name, qname, attributes):
        namespace,localname=name
        obj,schema=newRdfObject(namespace,localname,qname,attributes) #Also sets self.prefix and self.namespace
        self.subject=attributes['rdf:about']
        self.subject_type=qname
        self.subject_URI=
        uri, localname = name
        if localname == 'a':
            self.a_amount += 1
        if localname == 'b':
            self.b_amount += 1
    def characters(self, data):
        self.text = data