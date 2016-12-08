#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
import db
from mapper import mapper

def usage(status=0):
    print '''Usage: ./mapper_test.py [options]...

Options:
    -u URL      path of website to analyze (ex: http://www.wsj.com/)
    -o          output data to stdout
    -h          help'''
    sys.exit(status)

# main execution
if __name__ == '__main__':
    try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-h':
            usage(1)

    words = mapper('http://michaelsills.com/sample_links.html')
    for word,count in words.iteritems():
            print word + ' ' + str(count)
