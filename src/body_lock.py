
name = "locked"

def doData():
    print name + ".value " + str( 100 * getServerStatus()["globalLock"]["ratio"] )

def doConfig():
    host, port = extractHostPort()

    print "graph_title MongoDB write lock percentage (%s:%s)" % (host, port)
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    print name + ".label " + name





