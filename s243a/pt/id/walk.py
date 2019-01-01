import os, os.path
class ItemContainer:
    def __init__()
        self.items=[]
rootDir='/root/Downloads/pt'
for dirName, subdirList, fileList in os.walk(rootDir):
    items_path=os.join(dirname,"list.p")
    items_path2=Path(str(items_path)
    if items_path2.is_file():
        ic=ItemContainer()
        ic2=[]
        loadList(items_path2,ic)
        for item in ic.items:
            ic2.append(on_item(item))
def PT_bookmark_handler(item,out_items):
    if hasaattr(item,"href"):
        url=item.href
        a_pattern=r'(?P<protocol>[a-zA-Z]+)\:\/\/(?P<domain>[^/]+)\/(?P<path>.+)'
        m=re.match(a_pattern,url)
        matches=m.groupdict() 
        if matches[domain]=='www.pearltrees.com':        
          folders=[]
          last_path=matches['path']
          while True:
            a_pattern=r'(?P<folder>[^/#]+)(?P<sep>[#/])(?P<path>.+)'
            m=re.match(a_pattern,last_path)
            if bool(m):
                matches=m.groupdict() 
                folders.append(matches['folder'])
                last_path=matches['path']
                last_sep=matches['sep']
            else:
                break
          a_pattern=r'(?P<item_type>[a-zA-Z]+)(?P<item_id>[0-9]+)'
          m=re.match(a_pattern,last_path)
          if bool(m):
              matches=m.groupdict() 
              if (matches['item_type']=='item') and (last_sep==r"/'): #Item is a note
              elif (matches['item_type']=='id') and (last_sep==r"/'): #Item is a folder
              elif (matches['item_type']=='item') and (last_sep==r"#'): #Item is a URL (AKA pearlpage)
        else #Item is a URL (AKA Pearlpage or seperator)         
            
    