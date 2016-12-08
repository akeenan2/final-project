#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from mapper import mapper
from sort import sort
import db


def usage(status=0):
    print '''Usage: ./bench.py [options]...

Options:
    -u URL      url of website to analyze
    -s SORT     sorting algorithm [quick|merge|bst]
    -o          output the data
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
        opts,args = getopt.getopt(sys.argv[1:], "u:s:oh")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-u':
            URL = a
        elif o == '-s':
            SORT = a
        elif o == '-o':
            OUTPUT = True
        else:
            usage(1)

    if URL == '' or URL not in db.url_map:
        usage(1)

    # get the list of unsorted words
    words = mapper(URL)
    # run the sorting algorithm
    sorted_words = sort(words,SORT)
    # print results
    if OUTPUT:
        for word in sorted_words:
            print word[0] + ' ' + str(word[1])
