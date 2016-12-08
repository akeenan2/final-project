#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'../src')
import getopt
from mapper import *
import db


def usage(status=0):
    print '''Usage: ./sort_test.py [options]...

Options:
    -h          help'''
    sys.exit(status)

# default values
SORT = ''
URL = ''
OUTPUT = False

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        usage(1)

    for url in db.urls:
        # get the unsorted words
        words = mapper(url)
        for sort in SORT:  
            # run the sorting algorithm
            sorted_words = sort(words,SORT)
    # print results
    if OUTPUT:
        for word in sorted_words:
            print word[0] + ' ' + str(word[1])
