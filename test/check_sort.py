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
FILE = ''

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts,args = getopt.getopt(sys.argv[1:], "f:h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == "-f":
            FILE = a
        else:
            usage(1)

    if FILE == '':
        usage(1)

    curr = 1 # minimum count
    with open(FILE,'r') as f:
        for line in f:
            next = int(line.split(' ')[1])
            # next number in sorted order
            if next > curr:
                curr = next
            # if the next number is a smaller number
            elif next < curr:
                print >> sys.stderr,'the file is not sorted!'
                exit(1)
