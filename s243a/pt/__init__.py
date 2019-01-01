import sys
rootPath = r"/root/projects/pytest/"
#https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run
if not (rootPath in sys.path):
    print("Appending "+rootPath)
    sys.path.append(rootPath)

from s243a.pt.netscape import BookMarkParser

def pt_HTML_to_WebSite(**kw):
    p = BookMarkParser()
    filename=kw.get('filename','/root/Downloads/pearltrees_export.html')
    f = open(filename, "r")
    #BUFSIZE = 8192
    while True:
        #data = f.read(BUFSIZE)
        data=f.readline()
        print('data='+str(data))
        if not data: break
        p.feed(data)
    p.close(  )
    
filename='/root/Downloads/pearltrees_export.html'
pt_HTML_to_WebSite(filename=filename)