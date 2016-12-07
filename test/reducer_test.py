#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'../src')
import getopt
import db

def usage(status=0):
    print '''Usage: ./reducer_test.py [options]...

Options:
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

    for url in db.urls:
        os.system('python src/reducer.py -u {} -o'.format(url))
