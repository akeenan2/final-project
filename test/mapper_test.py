#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from mapper import mapper

def usage(status=0):
    print '''Usage: ./mapper_test.py'''
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

    # call mapper with demo url
    keywords = mapper('http://michaelsills.com/sample_links.html')

    # print results
    for word,count in keywords.iteritems():
        print word + ' ' + str(count)
