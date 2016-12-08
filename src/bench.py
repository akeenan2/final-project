#!/usr/bin/env python2.7
import os
import sys
import getopt
from mapper import *
import db

def usage(status=0):
    print '''Usage: ./sort_bench.py [options]...

Options:
    -h          help'''
    sys.exit(status)

# defaults
SORT = ['sort','quick','merge','bst']

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

    for url in db.urls:
        for s in SORT:
            os.system("./measure ./sort.py -u {} -s {} -o".format(url,s))
