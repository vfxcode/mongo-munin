
import urllib2
import sys
import os

try:
    import json
except ImportError:
    import simplejson as json

def extractHostPort():
    basename = os.path.basename(__file__).rsplit('_')[-1]
    host, port = basename.split(':')
    return (host, port)

def getServerStatus():
    host, port = extractHostPort()
    url = "http://%s:%s/_status" % (host, port)
    req = urllib2.Request(url)
    raw = urllib2.urlopen(req).read()
    return json.loads( raw )["serverStatus"]

getServerStatus()
