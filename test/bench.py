#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from mapper import mapper
import db

def usage(status=0):
    print '''Usage: ./sort_test.py [options]...

Options:
    -h          help'''
    sys.exit(status)

# default values
SORTS = ['default','quick','merge','bst']
OUTPUT = False

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts,args = getopt.getopt(sys.argv[1:], "oh")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-o':
            OUTPUT = True
        else:
            usage(1)

    for sort in SORTS:
        print sort
        for url in db.urls:
            # run the bench script
            if OUTPUT:
                os.system("./src/measure ./test/run_sort.py -u {} -s {} -o".format(url,sort))
            else:
                os.system("./src/measure ./test/run_sort.py -u {} -s {}".format(url,sort))
        print '\n',