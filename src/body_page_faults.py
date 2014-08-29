name = "page_faults"

def doData():
    print name + ".value " + str( getServerStatus()["extra_info"]["page_faults"] )

def doConfig():
    host, port = extractHostPort()

    print "graph_title MongoDB page faults (%s:%s)" % (host, port)
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel page_faults / ${graph_period}"
    print "graph_category MongoDB"

    print name + ".label " + name
    print name + ".min 0"
    print name + ".type COUNTER"
    print name + ".draw LINE1"





