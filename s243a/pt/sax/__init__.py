import xml.sax

class InkscapeSvgHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        if name == "svg":
            for (k,v) in attrs.items():
               print k + " " + v
 
parser = xml.sax.make_parser()
parser.setContentHandler(InkscapeSvgHandler())
parser.parse(open("svg.xml","r"))