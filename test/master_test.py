#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from master import master

def usage(status=0):
    print '''Usage: ./master_test.p'''
    sys.exit(status)
    
# main execution
if __name__ == '__main__':
    # parse options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        usage(1)

    # call master function with demo urls
    keywords = master([
        "http://michaelsills.com/sample_links.html",
        "http://michaelsills.com/sample_links_2.html"
    ])
    
    # print results
    for word in keywords:
        print word[0] + ' ' + str(word[1])
