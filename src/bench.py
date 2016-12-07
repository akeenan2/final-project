#!/usr/bin/env python2.7
# bench.py
# runs the different sorts on the results of mapper.py and times each one

import os
import sys
import getopt
from mapper import *
import db # from db.py

#defaults
SORT = ['sort', 'quick', 'merge', 'bst']
FILE = ['abcnews', 'dailymail', 'forbes', 'google', 'huffingtonpost', 'nytimes', 'theguardian', 'usatoday', 'washingtonpost', 'wsj']

# main execution
if __name__ == '__main__':
    for f in FILE:
    	print f
    	for s in SORT:
    		print s
    		os.system("./measure ./sort.py -f ../data/{}-map.txt -s {}".format(f, s))