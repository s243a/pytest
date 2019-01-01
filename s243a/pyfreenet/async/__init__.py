#class SimplePyGreenlet:
from  s243a.freenet.async.util import *  
def catchResult(a,obj=None):
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
    
loggerCallBacks={'put':lambda obj,a: print(a),
                 'catchResult' obj,a: catchResult(a,obj),
                 'waitingMSG' obj,a: print "Waiting" + datetime.now().strftime('%s(s) %m/%d/%Y')}
   
class SimpleFeeBottleJob:

    #self.job = None #A freenet job
    #self.g = None
    #self.body = None
    #self.OutputType =None
    
    def __init__(self,job_or_uri=None,**kw):
        self.kw={}
        self.kw['message']=kw.get('message',None)
        self.kw['file']=kw.get(file,None)
        self.loggerContainer=kw.get('loggerContainer',None)
        #if self.loggerContainer is not None and self.node is not None:
        #    self.loggerContainer.node=node
        self.host=kw.get('host',"127.0.0.1")
        self.port=self.kw.get('port',9481)
        self.OutputType=self.kw.get('OutputType','HTML')
        #selffcpPort,aBody,OutputType
        if job_or_uri is not None:
            if type(job_or_uri) is str:
                print("__init__" + "uri as input")
                if job_or_uri in jobs:                
                    print("uri in jobs")
                    self.job=jobs[job_or_uri]
                else:
                    print("making job")
                    node = fcp.FCPNode(fcpHost,verbosity='fcp.DETAIL',port=self.kw)
                    val = self.kw['message'] 
                    ksk = job_or_uri
                    uri = "KSK@" + ksk
                    node.put("KSK@"+ksk, data=val, mimetype="text/plain", verbosity=fcp.DETAIL)
                    #self.job = node.get(uri, async=True)
                    self.startCB = lambda: node.get(uri, async=True) #A start callback is safer than immediatly starting the job
            else:
                print("__init__"+"job as input")
                print("Warning: Make sure that logger is created before job is started")
                self.job=job_or_uri
                self.startCB = lambda: job_or_uri #Best of luck with this! Job might proceed before logger is ready.
        if self.OutputType == "HTML":
            self.Brk="<br>"
        elif self.OutputType == "UNIX":
            self.Brk="" #We won't use "\n" since print automatically generates the \n. Write can be used instead if one wants to explicitly use the /n
        self.loggerContainer=kw.get('loggerContainer',None)
        self.body=kw.get('body',None)
        if self.body is None:
            try:
                self.body = self.loggerContainer.body   
            except:
                print("Warning: body should be set in logger before freenet worker is created")
                self.body = queue.Queue()
        self.greenlet=kw.get('greenlet',None)
        if self.greenlet is None:
            g = Greenlet(self.on_data)
        try:
            if self.loggerContainer.body is None:
                if self.body is not None:
                    self.loggerContainer.body=self. body
        except:
            pass

        #self.setBody(kw.get('body',None)) # Replaced w/ the above code
        self.startCB=kw.get('startCB',None) #Maybe I need to define a default start CB.    
        
    def on_data(self):
        # we can poll the job
        while True:
            val, ready = self.loggerContainer.readBuf()
            if ready: 
                print val
                self.body.put(val)    
            if self.loggerContainer.isComplete():
                print "Yay! job complete"
                
                try:
                    self.body.put(self.job.getResult()) #Returns the completion message.
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst.args)     # arguments stored in .args
                    print(inst)          # __str__ allows args to be printed directly,
                    break        
            else:
                print "Waiting" + datetime.now().strftime('%s(s) %m/%d/%Y')+self.Brk
                #self.body.put("Waiting" + datetime.now().strftime('%s(s) %m/%d/%Y')+self.Brk)
                time.sleep(0.001) #Yield control to other threads
                gevent.sleep(7) #This yields control to another greenlet
        print("Apparently we are done!")
        self.on_finish() #Maybe we can sequence the greenlets instead of putting this here.
        
    def on_finish(self):
        self.body.put('</body></html>') #There should be a way to seperate these last two lines from this method.
        self.body.put(StopIteration)
    def header(self,start_response=None):
        if self.OutputType == "HTML":
            if start_response is not None:
                start_response('200 OK', [('Content-Type', 'text/html')])
        self.body.put(' ' * 1000)
        if self.OutputType == "HTML":
            self.body.put("<html><body><h1>Current Time:</h1>")   
           
    def handle(self,environ=None, start_response=None,aBody=None):
        lambda a: self.start(self,enviorn,start_response)
        #g = Greenlet.spawn(on_data, body)
    def setBody(self,aBody=None,aGreenlet=None):
        if aBody is None:
           if self.body is None: 
               print("setting body & greenlet. Normally we shouldn't do this here")
               self.body = queue.Queue()
               self.greenlet = Greenlet(self.on_data) 
               self.loggerContainer.body=self.body
        else:
           self.body = aBody
        if aGreenlet is None:
            if self.greenlet is None:
                self.greenlet = Greenlet(self.on_data)
        else:
            self.greenlet=aGreenlet
        if self.loggerContainer.body is None:
            self.loggerContainer.body=self.body
    def start(self,environ=None, start_response=None,aBody=None,aGreenlet=None): # Not sure
        #https://stackoverflow.com/questions/20824218/how-to-implement-someasyncworker-from-bottle-asynchronous-primer
        #g = Greenlet.spawn(current_time, lambda a: on_data(body))
        print("Set Body")
        self.setBody(aBody)
        print("header")
        self.header(start_response)
        self.job=self.startCB() #Maybe add the option for some key words (i.e. kw) to the startCB function
        print("start")
        self.greenlet.start()            
        return self.body, self.greenlet


class LoggerContainer:
    def __init__(self,node=None,**kw):
        self.ready = False
        self.strBuff = StringIO.StringIO()
        self.job = kw.get('job',None)
        self.Brk = kw.get('Brk',"\n")
        self.body = kw.get('body',None) #The html body to write to.

        self.msgDict={}
        self.meseges=[None]*5
        self.msgPosNext=0
        self.msgPos=-1
        self.msgMax=5
        self.msgLnCnt=0  
        self.cb = kw.get('cb',None) #A callback function for self.logfunc
        self.node=kw.get('node',None)
        self.dealayDuringFetch=7
        self.delayWhenFishished=100
        self.complete=False         
        self.EndHdr=False
        
    def do_logfunc(self,msgline):
        #print("self.msgPosNext="+str(self.msgPosNext))
        
        self.meseges[self.msgPosNext]={ "msg_str" : msgline,
                                        "time" : datetime.now()
                                      }      
        self.msgPos=self.msgPosNext
        #print("self.msgMax="+str(self.msgMax))
        self.msgPosNext=((self.msgPosNext+1)%(self.msgMax))
        if self.filterMSG(msgline):
            self.msgDict[msgline]=datetime.now()
        if self.msgLnCnt<self.msgMax:
            self.msgLnCnt=self.msgLnCnt+1         
    def logfunc(self,msgline,**kw):
        #print(msgline)
        mDict=self.parseMsg(msgline)
        #cb=None,HTML_lb="<br>"
        #if cb is None:
        #    cb=lambda msg: self.print_and_put_cb(msg,HTML_lb="<br>",chkSender=True)
   
        if self.cb is None:
            #print(msgline)
            self.print_and_put_cb(msgline,mDict)
        else:
            cb(msgline,mDict) 
        self.do_logfunc(msgline)             
    def parseMsg(self,msg):
        mDict=self.parseSenderLine(msg)
        sender=mDict.get('sender',None)
        if (sender == 'CLIENT') or (sender == 'CLIENT'):
            mDict['node_or_client']=True
            try: #Not sure if we need a try/except here
                #k, v = mgStrToKey(mDict['msg_str'])
                #mDict['k']=v
                mDict=self.parseFCPMsgStr(mDict['msg_str']) # I haven't decided if a dictionary should be returned or a seperate key/value
            except:
                pass
        return mDict    
    def parseSenderLine(self,msg_line):
       regex=r'^(?P<sender>\S+)[:]\s+(?P<msg_str>[^\n]+)\n{0,1}$'
       try: #Not sure if we need a try/except here
           #print msg_line
           m=re.match(regex,msg_line)
           mDict=m.groupdict()
           assert len(mDict['msg_str'])>0 #,"Could not parse msg_str"
           self.setStatus(mDict['msg_str']) #This is to detect the end of communications
       except AssertionError:
           print("Could not parse msg_str")
           print("msg_line="+msg_line)
           return mDict
       if mDict is None:
           mDict={'sender' : 'Unknown',
                 'msg_str' : msg_line } 
       return mDict
    def parseFCPMsgStr(self,msg_line): #I should think of a better name for this
        mDict, succeeded = self.parseSenderLine(msg_line)
        if succeeded:
            k, v, hasKeyVal = line.split("=", 1)
            if hasKeyVal:
                mDict['parsed'][k]=v
            else:
                mDict['parsed'][mDict['msg_str']]=True #Maybe do some checks here such as length and for white space characters
        return mDict, succeeded
    def print_and_put_cb(self,msg,mDict):
        node_or_client=mDict.get('node_or_client',False)
        #chkSender= not node_or_client
        if self.filterMSG(msg): #Don't reprint the same message if we've scene it recently.
            print self.msg_to_str(msg)
        if node_or_client:
            self.bodyPut_cb(msg,chkSender=False)
    def filterMSG(self,msg): #We don't want to see the same log message too often
        t1=self.msgDict.get(msg,None)
        
        if t1 is not None: #isinstance(t1,datetime): 
            if self.isComplete():
                delay=self.delayWhenFishished=100
            else:
                delay=self.dealayDuringFetch=7
            t2=datetime.now()
            delta = t2 - t1 #https://stackoverflow.com/questions/2880713/time-difference-in-seconds-as-a-floating-point
            #print(str(delta.seconds)+" "+msg)            
            if delta.seconds>delay:
                return True
            else:
                return False
        else:
            #print("New Message"+msg)
            return True
    def bodyPut_cb(self,msg,HTML_lb="<br>",chkSender=True):
        #parseMsg
        if chkSender:
            if self.filterForBody(msg):
                print('bodyPut_cb: This branch should not normally be called')
                self.body.put(self.msg_to_str(msg)+HTML_lb)
        else:
            self.body.put(self.msg_to_str(msg)+HTML_lb)
            
    def filterForBody(self,msg):
        if msg.startswith("NODE:") or msg.startswith("CLIENT:"):
            return True
        else:
            return False

    def msg_to_str(self,msg):
        if type(msg) == str:
            return msg
        elif type(msg) is dict: #isinstance(msg, collections.Mapping): #https://stackoverflow.com/questions/25231989/how-to-check-if-a-variable-is-a-dictionary-in-python
            return msg['msg_str']
        else:
            return "Empty Message"
    def tail(self,lines=0,cb=None,delta=None):
        if cb is None:
            cb=self.print_and_put_cb
        if lines == 0:
            N=self.msgMax
        else:
            N=min(self.msgMax,lines)
        for i in range(self.msgPost,self.msgPos-N+1,-1):
            msg_i=self.meseges[i%self.msgMax]
            if delta is not None:
                t2=datetime.now()
                t1=msg_i['time']
                delta2=t2-t1
                if delta2.delta.microseconds > delta.microseconds:
                    break
            cb(self.meseges[i%self.msgMax])
                 
        #self.body.put(msgline)  
    def myLogger(self, level, msg):
        print("level="+level + " msg=" + msg)
        if level > self.job.verbosity:
            return   
        if not msg.endswith(self.Brk):
            msg += "\n"
        
        strBuff.write(msg)
        self.isReady = True
        #strBuff.flush()
        #time.sleep(0.001)
    def getLogger(self): #THis might be redundant
        return self.myLogger               
    def isReady(self):
        return self.ready
    def flush(self):
        val=self.strBuff.getvalue()
        self.strBuff.close()
        self.strBuff = StringIO.StringIO()
        self.isRead=False
        return val
    def getValue(self):
        self.strBuff.getValue()
    def readBuf(self):
        if self.ready:
            val = self.flush()
            ready = True
            return val, ready
        else:
            ready = False
            val = ""
            return val, ready
        return val, ready
    def isComplete(self): # We might also want to check for an EndMessage and wait if needed
        return self.complete
        #if self.job.msg['hdr'] == 'PutSuccessful':
        #    return True
        #elif self.job.msg['hdr'] == 'PutFailed':
        #    return True
    def detectEndMsg(self,msg): #I don't think we use this
        
        if filterForBody(self,msg):
            node_or_client = True
        else:
            node_or_client = False
        return node_or_client
    def setStatus(self,msgLine):
        if msgLine == 'PutSuccessful':
            self.EndHdr=True
        elif msgLine == 'PutFailed':
            self.EndHdr=True
        if self.EndHdr==True:
            if msgLine=='EndMessage':
                self.complete=True
    def callback(self, status, value):
        if status == 'PutSuccessful':
            self.complete=True
        elif status == 'PutFailed':
            self.complete=True
        #elif status == 'URIGenerated':
        #    self.complete=True        
        #self.msg=value
    def getCallback(self):
        return self.callback     
class FeeBottleJob:

    #self.job = None #A freenet job
    #self.g = None
    #self.body = None
    #self.OutputType =None
    
    def __init__(self,job_or_uri=None,**kw):
        self.kw={}
        self.kw['message']=kw.get('message',None)
        self.kw['file']=kw.get(file,None)
        self.loggerContainer=kw.get('loggerContainer',None)
        #if self.loggerContainer is not None and self.node is not None:
        #    self.loggerContainer.node=node
        self.host=kw.get('host',"127.0.0.1")
        self.port=self.kw.get('port',9481)
        self.OutputType=self.kw.get('OutputType','HTML')
        #selffcpPort,aBody,OutputType
        if job_or_uri is not None:
            if type(job_or_uri) is str:
                print("__init__" + "uri as input")
                if job_or_uri in jobs:                
                    print("uri in jobs")
                    self.job=jobs[job_or_uri]
                else:
                    print("making job")
                    node = fcp.FCPNode(fcpHost,verbosity='fcp.DETAIL',port=self.kw)
                    val = self.kw['message'] 
                    ksk = job_or_uri
                    uri = "KSK@" + ksk
                    node.put("KSK@"+ksk, data=val, mimetype="text/plain", verbosity=fcp.DETAIL)
                    #self.job = node.get(uri, async=True)
                    self.startCB = lambda: node.get(uri, async=True) #A start callback is safer than immediatly starting the job
            else:
                print("__init__"+"job as input")
                print("Warning: Make sure that logger is created before job is started")
                self.job=job_or_uri
                self.startCB = lambda: job_or_uri #Best of luck with this! Job might proceed before logger is ready.
        if self.OutputType == "HTML":
            self.Brk="<br>"
        elif self.OutputType == "UNIX":
            self.Brk="" #We won't use "\n" since print automatically generates the \n. Write can be used instead if one wants to explicitly use the /n
        self.loggerContainer=kw.get('loggerContainer',None)
        self.body=kw.get('body',None)
        if self.body is None:
            try:
                self.body = self.loggerContainer.body   
            except:
                print("Warning: body should be set in logger before freenet worker is created")
                self.body = queue.Queue()
        self.greenlet=kw.get('greenlet',None)
        if self.greenlet is None:
            g = Greenlet(self.on_data)
        try:
            if self.loggerContainer.body is None:
                if self.body is not None:
                    self.loggerContainer.body=self. body
        except:
            pass

        #self.setBody(kw.get('body',None)) # Replaced w/ the above code
        self.startCB=kw.get('startCB',None) #Maybe I need to define a default start CB.    
        
    def on_data(self):
        # we can poll the job
        while True:
            val, ready = self.loggerContainer.readBuf()
            if ready: 
                print val
                self.body.put(val)    
            if self.loggerContainer.isComplete():
                print "Yay! job complete"
                
                try:
                    self.body.put(self.job.getResult()) #Returns the completion message.
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst.args)     # arguments stored in .args
                    print(inst)          # __str__ allows args to be printed directly,
                    break        
            else:
                print "Waiting" + datetime.now().strftime('%s(s) %m/%d/%Y')+self.Brk
                #self.body.put("Waiting" + datetime.now().strftime('%s(s) %m/%d/%Y')+self.Brk)
                time.sleep(0.001) #Yield control to other threads
                gevent.sleep(7) #This yields control to another greenlet
        print("Apparently we are done!")
        self.on_finish() #Maybe we can sequence the greenlets instead of putting this here.
        
    def on_finish(self):
        self.body.put('</body></html>') #There should be a way to seperate these last two lines from this method.
        self.body.put(StopIteration)
    def header(self,start_response=None):
        if self.OutputType == "HTML":
            if start_response is not None:
                start_response('200 OK', [('Content-Type', 'text/html')])
        self.body.put(' ' * 1000)
        if self.OutputType == "HTML":
            self.body.put("<html><body><h1>Current Time:</h1>")   
           
    def handle(self,environ=None, start_response=None,aBody=None):
        lambda a: self.start(self,enviorn,start_response)
        #g = Greenlet.spawn(on_data, body)
    def setBody(self,aBody=None,aGreenlet=None):
        if aBody is None:
           if self.body is None: 
               print("setting body & greenlet. Normally we shouldn't do this here")
               self.body = queue.Queue()
               self.greenlet = Greenlet(self.on_data) 
               self.loggerContainer.body=self.body
        else:
           self.body = aBody
        if aGreenlet is None:
            if self.greenlet is None:
                self.greenlet = Greenlet(self.on_data)
        else:
            self.greenlet=aGreenlet
        if self.loggerContainer.body is None:
            self.loggerContainer.body=self.body
    def start(self,environ=None, start_response=None,aBody=None,aGreenlet=None): # Not sure
        #https://stackoverflow.com/questions/20824218/how-to-implement-someasyncworker-from-bottle-asynchronous-primer
        #g = Greenlet.spawn(current_time, lambda a: on_data(body))
        print("Set Body")
        self.setBody(aBody)
        print("header")
        self.header(start_response)
        self.job=self.startCB() #Maybe add the option for some key words (i.e. kw) to the startCB function
        print("start")
        self.greenlet.start()            
        return self.body, self.greenlet
