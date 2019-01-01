import bottle
from bottle import route, run, Bottle
import sys, os, re, urllib
#fcpHost = "127.0.0.1"
#import fcp
#node = fcp.FCPNode(host=fcpHost, verbosity=fcp.DETAIL)

app = Bottle()

#m1="'"


def delim_filter(config):
    bottle.debug(True)
    print("Entering delim_filter")
    ''' Matches a comma separated list of numbers. '''
    aconfig = config or "%20"
    print ("aconfig=" + aconfig)
    delimiter = urllib.unquote(aconfig).decode('utf8') 
    print("delimiter=" + delimiter)   
    regexp = r'(?!{a_delim})+({a_delim}(?!{a_delim})+)*'.format(a_delim=re.escape(delimiter))
    print("regexp="+regexp)
    def to_python(match):
        print("Converting Match")
        print("Math=" + match)
        ms = map(urllib.unquote(aconfig).decode,match.split())
        print( "ms=" + ms )
        return ms

    def to_url(astr):
        print("Converting to URL")
        print ("astr=" + astr)
        astr2 = delimiter.join(map(urllib.unquote(aconfig).decode,astr))
        print("astr2="+astr2)
        print  astr2
        return astr2

    return regexp, to_python, to_url

app.router.add_filter('delim', delim_filter)

def split_urlArgs(url,delim=" ",
                  decode='All',
                  xfm_de=lambda a: urllib.unquote(a).decode('utf8'),
                  xfm_split=lambda a, b: re.split(a,b), #Typically a is a regular expression and b a string
                  fn_regexp = lambda a: r'(?!{a_delim})+({a_delim}(?!{a_delim})+)*'.format(a_delim=a) ):
    bottle.debug(True)
    ''' Matches a comma separated list of numbers. '''
    print("delimiter=" + delim)   
    if decode == "Args":
        ms = xfm_split(fn_regexp(a),url)
    elif decode == "All":
        url2 = xfm_de(url)    #Decode the URL
        delim= xfm_de(delim) #Decode the delimitor
        ms = xfm_split(fn_regexp(delim),url)
    elif decode == "None":
        ms = xfm_split(fn_regexp(delim),url) #SPlit the URL based on a regular expression.
            
    print( "ms=" + "["+",".join(ms) +"]" )    
    return ms, delim

def combine_urlArgs(args,delim=" ",
                    encode='All',
                    xfm_encode=lambda a: urllib.quote(a, safe=''),
                    xfm_join=lambda a, b: a.join(b)): #Typically a is the delimiter and b is a list
    print("Converting to URL")
    print ("astr=" + args)
    if decode == "Args":
        astr2 = xfm_join(delim,(map(lambda a: xfm_encode,args)))
    elif decode == "All":
        astr2 = urllib.unquote(xfm_join(delim,args))
    elif decode=="None":
        astr2 = xfm_join(delim,args)      
    print("astr2="+astr2)
    return astr2    
 

#@app.route('/<key>/%09/<cmd>/<args:delim:%09>') # %09 == tab
#@app.route('/<key>/%20/<cmd>/<args:delim:%20>') # %20 == ' '
#@app.route('/<key>/ /<cmd>/<args:delim: >') # %20 == ' '
#@app.route('/<key>/%3B/<cmd>/<args:delim:%3B>') # %3B == ';'
#@app.route('/<key>/;/<cmd>/<args:delim:;>') # %3B == ';'
#@app.route('/<key>/%2C/<cmd>/<args:delim:%2C>') # %2C == ','
#@app.route('/<key>/,/<cmd>/<args:delim:,>') # %2C == ','
@app.route('/<key>/<sep>/<cmd>/<args:path>') # %2C == ','
def mystery(key,cmd,args,sep=""):
    bottle.debug(True)
    print("engering mystery")
    print("sep=" + sep)
    if len(sep) > 0 : # True if seperator is a wild card
        args, sep = split_urlArgs(args,sep)
    if key == '1234': # %2C == ','
        print(key)
        print(cmd)
        print(args)
        #delimiter = urllib.unquote(aconfig).decode('utf8')
        #print(delimiter)            
        result1 = os.popen("IFS=<a_dilim>".format(a_dilim=sep)).read()
        print("result1=" + result1)
        result2 = result1 + "<br>"
        print("result2=" + result2)     
        cmd_str=cmd + sep + sep.join(args)
        print(cmd_str)   
        result3 = result2 +os.popen(cmd_str).read()
        print("result3=" + result3)               
        return "<pre>" + result3 + "</pre>"
        #return result3.replace("\n","<br>")
        #return ('key=' + key + '<br>' +
        #     'sep=' + sep + '<br>' +
        #     'cmd=' + cmd + '<br>' +
        #     'args='   + "[" + ",".join(args)+"]") 
#@app.route('/USK@<hashKey:nocomma>,<ecryptionKey:nocomma>,<encryption:nocomma>/<metaData:path>')
#def hello(hashKey,ecryptionKey,encryption,metaData):
#    
#    mimetype, val1 = node.get(uri)
#    return ('hashKey=' + hashKey + '<br>' +
#             'ecryptionKey=' + ecryptionKey + '<br>' +
#             'encryption=' + encryption + '<br>' +
#             'metaData='   + metaData) 
#             
#Regular eressions use a seperate filter; https://bottlepy.org/docs/dev/routing.html
app.run(host='localhost', port=8082, debug=True)