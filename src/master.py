#!/usr/bin/env python2.7
import sys
import time
from collections import Counter
import db
from mapper import mapper
from sort import sort

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
	-u URLS     list of urls 
    -o          output data to stdout
    -h          help'''
    sys.exit(status)

def master(urls):
    master = Counter()
    # call mapper on all urls and reduce to one master dict
    for url in urls:
        temp_dict = Counter(mapper(url))
        master = master + temp_dict
    # sort by count
    master = sort(master)
    return master

OUTPUT = False

# main execution
if __name__ == '__main__':
    # parse options
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
    # call master function
    words = master(db.urls)
    # print results
    if OUTPUT:
        for word in words:
            print word[0] + ' ' + str(word[1])
