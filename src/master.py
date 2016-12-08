#!/usr/bin/env python2.7
import sys
import time
import getopt
from collections import Counter
import db
import getopt
from mapper import mapper
from reducer import reducer
from sort import sort

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
	-s SORT 	type of sort to use
    -o          output data to stdout
    -h          help'''
    sys.exit(status)

def master():
    master_dict = Counter()
    # call mapper on all urls and append results
    for url in db.urls:
        temp_dict = Counter(mapper(url))
        master_dict = master_dict + temp_dict
    # compile counts of all words
    master_dict = reducer(master_dict)
    # sort by count
    master_dict = sort(master_dict)
    return master_dict

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
    words = master()

    # print results
    if OUTPUT:
        for word in words:
            print word[0] + ' ' + str(word[1])
    # pull out top 10 most frequent words
    print "Top Words:"
    trending = words[:-11:-1]
    for word in trending:
    	print word[0] + ' ' + str(word[1])