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
SORT = ['sort', 'quick', 'merge', 'bst']
FILE = ['abcnews', 'dailymail', 'forbes', 'google', 'huffingtonpost', 'nytimes', 'theguardian', 'usatoday', 'washingtonpost', 'wsj']

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

    for u in db.urls:
    	print u
    	for s in SORT:
    		print s
    		os.system("./measure ./sort.py -u {} -s {}".format(u, s))
