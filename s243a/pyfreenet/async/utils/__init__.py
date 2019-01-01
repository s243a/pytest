def freeJobFactory(obj=None,**kw):
    fcpHost=request.json.get('host','127.0.0.1')
    fcpVerbosity=request.json.get('verbosity',fcp.NOISY)
    fcpPort=request.json.get('port',9481)
    if out is not None:
        out=obj
    else
    out.{}
    out.host=kw.get('host',"127.0.0.1"): kw.pop('host',None)
    out.verbosity=fcp.NOISY: kw.pop('verbosity',None)
    out.port=self.kw.get('port',9481): kw.pop('port',None)
    out.kw['message']=kw.get('message',None): kw.pop('message',None)
    out.kw['file']=kw.get(file,None): kw.pop('file',None)
    out.loggerContainer=kw.get('loggerContainer',None)
    out.OutputType=self.kw.get('OutputType','HTML'): kw.pop('OutputType')
    #selffcpPort,aBody,OutputType
    job=fm_job_or_uri(pop=True,kw=kw)

#python has a weird syntax for functions ifs. See: https://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda
iff=lambda a,b,c: b if a else c
#Set a value for a dictonary if it doesn't exist
alt=lambda d,k,a: a.get(k,None) if a.get(k,None) is not None else b #d=dict, k=key,a=alternate value
call_if=lambda a b: b() if a else b 
def mk_node(**kw):    
    set_node_defaults(kw)
    kw.node=alt(kw,'node',fcp.FCPNode(kw.fcpHost,verbosity=kw.verbosity,port=kw.port))    
def set_node_defaults(**kw):
    kw.verbocity=alt(kw,'verbocity','fcp.DETAIL')
    kw.port=alt(kw,'port',9481)
    kw.fcpHost=alt(kw,'fcpHost','127.0.0.1')
    kw.mimetype=alt(kw,'mimetye',"text/plain") #TODO add logic to try to deduce mime type before setting it to "test/plain"
    kw.async=alt(kw,'async',True)
def add_kws(kw1,*kw):
    for k,v in kw:
        kw1=alt(kw,k,v) ##We anly add the value if it doesn't exist. Might want to change this to throw an exception
def job_fm_str(uri,jobs=None,node=None,message=None,path=None,**kw): //appends missing items to kw
     
    if (uri in jobs) and (jobs is None):                
        out.job=jobs[job_or_uri] #TODO check the format of the URI before doing this lookup
        return job
    if node is None:    
        node=mk_node(kw)
    else:
        add_kws(kw,job,node,message)
        set_node_defaults(kw)
        if kw.get(node,None) is None:
        uri=add_key_type_prefix(uri)
        message=kw.get('message',None)
        path=iff('path' is not None,path,kw.get('file',None))
        if message is not None:
            
            call_if(async=False,
            if async=True:        
                kw.startCB = labmda: out.node.put(uri, nessage, mimetype=kw.mimetype, verbosity=kw.verbosity)
            else:
                kw=out.node.put(uri, nessage, mimetype=kw.mimetype, verbosity=kw.verbosity)
        elif path is not None
            kw.startCB = labmda: out.startCB(uri, file=path, mimetype=kw.mimetype, verbosity=kw.verbosity)
        else
            kw.startCB=lambda: node.get(uri, kw.async)
    #self.job = node.get(uri, async=True)
    out.startCB =  #A start callback is safer than immediatly starting the job        
def add_key_type_prefix(uri)
    if (not uri.startswith('KSK@') and
       (not uri.startswith('USK@') and
       (not uri.startswith('CHK@'):
        #ksk = job_or_uri
        return = "KSK@" + uri
    else
        return uri

def fm_job_or_uri(job_or_uri=None,pop=True,kw)
    if job_or_uri is None:
        job=kw.get(job,None):
        if job is None:
            job is None
    if job_or_uri is not None:

        else:
            //print("__init__"+"job as input")
            //print("Warning: Make sure that logger is created before job is started")
            out.job=job_or_uri
            out.startCB = lambda: job_or_uri #Best of luck with this! Job might proceed before logger is ready.
    if out.OutputType == "HTML":
        out.Brk="<br>"
    elif self.OutputType == "UNIX":
        out.Brk="" #We won't use "\n" since print automatically generates the \n. Write can be used instead if one wants to explicitly use the /n
    out.loggerContainer=kw.get('loggerContainer',None)
    #The following commented out stuff is a special case so it is removed. 
    #out.body=kw.get('body',None)
    #if out.body is None:
    #    try:
    #        out.body = self.loggerContainer.body   
    #    except:
    #        //print("Warning: body should be set in logger before freenet worker is created")
    #        out.body = queue.Queue()
    #self.greenlet=kw.get('greenlet',None)
    #if self.greenlet is None:
    #    g = Greenlet(self.on_data)
    #try:
    #    if self.loggerContainer.body is None:
    #        if self.body is not None:
    #            self.loggerContainer.body=self. body
    #except:
    #    pass
