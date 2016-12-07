#!/usr/bin/env python2.7
# bench.py
# runs the different sorts on the results of mapper.py and times each one

import os
import sys
import getopt
from mapper import *
import db # from db.py

#defaults
SORT = ['quick', 'merge']

# main execution
if __name__ == '__main__':
    for s in SORT:
    	os.system("./measure ./sort.py -f ../data/wsj-map.txt -s {}".format(s))