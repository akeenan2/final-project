#!/usr/bin/env python2.7
import time
from collections import Counter
import db
import getopt

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
	-s SORT 	type of sort to use
    -h          help'''
    sys.exit(status)

def master():
	master_dict = Counter()
	# urls 
	for url in db.urls:
		temp_dict = Counter(mapper(url))
		master_dict = master_dict + temp_dict
		
	master_dict = reducer(master_dict)
	master_dict = sort(master_dict, SORT)
	
	time.sleep(10)
#defaults
SORT = 'default'

# main execution
if __name__ == '__main__':
	#parse options
	try:
        opts,args = getopt.getopt(sys.argv[1:], "s:h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
    	if o == '-s':
    		SORT = a
    	else:
    		usage(1)
	
	master()