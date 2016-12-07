#!/usr/bin/env python2.7
import os
import sys
import getopt
from mapper import *
import db # from db.py

def usage(status=0):
    print '''Usage: python generate-maps.py [options]...

Options:
    -h          help'''
    sys.exit(status)

#defaults
SORT = ['quick', 'merge']

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

    for s in SORT:
    	os.system("./measure ./sort.py -f ../data/wsj-map.txt -s {}".format(s))