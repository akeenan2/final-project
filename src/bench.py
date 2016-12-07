#bench.py
#runs the different sorts on the results of mapper.py and times each one

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
    	command = "./measure python sort.py -f ../data/wsj-map.txt -s " + s
    	os.system(command)