#! /usr/bin/env python
import sys, os
import fcp
from s243a.pyFreenet.async import FreeWorkerFactory
cpHost = "127.0.0.1"
Download_Folder="/root/spot/Downloads"
async=True
#one only needs to define the uris to download, the other fields are optional
URIs=[ {'uri':usk@, 'async'=True, description='FILP-source'},
       {'uri':usk@, 'async'=True, description='32bit FILP build'}]

def saveDownload(file,path,async=False,job=job):
    # write our string to a file
    if async:
        job.isComplete()
    else
        f = file(path, "w")
        f.write(val)
        f.close()

node = fcp.FCPNode(host=fcpHost, verbosity=fcp.DETAIL)

if async:
    job = node.get(uri, async=True)
else:
    mimetype, val1 = node.get(uri, async=async)

path=Download_Folder+uri

greenlet = Greenlet(self.on_data)


# ------------------------------------------
# now, demonstrate asynchronous requests

print "Launching asynchronous request"
job = node.get(uri, async=True)

# we can poll the job
if job.isComplete():
    print "Yay! job complete"
else:
    # or we can await its completion
    result = job.wait()

print "Result='%s'" % str(result)

# ------------------------------------------
# similarly, we can get to a file

path = raw_input("temporary file to retrieve to: ")
node.get(path, file=path)

# again, the 'file=' can be a pathname or an open file object

# ------------------------------------------
# TODO: demonstrate persistent requests

# ------------------------------------------
# TODO: demonstrate global requests