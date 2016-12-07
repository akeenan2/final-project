#!/usr/bin/env python2.7
import time
from collections import Counter
import db

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
    -h          help'''
    sys.exit(status)

def master():
	master_dict = Counter()
	# urls 
	for url in db.urls:
		temp_dict = Counter(mapper(url))
		master_dict = master_dict + temp_dict
		
	master_dict = reducer(master_dict)
	master_dict = sort(master_dict)
	
	time.sleep(10)
#defaults


# main execution
if __name__ == '__main__':
	#parse options
	try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
    	usage(1)
	
	master()