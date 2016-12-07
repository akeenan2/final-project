#!/usr/bin/env python2.7
import time
from collections import Counter
import db

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
	-f 			use files
    -h          help'''
    sys.exit(status)

def master(use_file):
	master_dict = Counter()
	if use_file == 1:
		with open(FILE,'r+') as f:
	        # build a dictionary from the file
	        for line in f:
	            l = line.split(' ')
	            WORDS[l[0]] = l[1].rstrip()
	        f.close()

	else:
		# urls 
		for url in db.urls:
			temp_dict = Counter(mapper(url))
			master_dict = master_dict + temp_dict
			
		master_dict = reducer(master_dict)
		master_dict = sort(master_dict)
	
	time.sleep(10)
#defaults
USE_FILE = 0
FILE = ''

# main execution
if __name__ == '__main__':
	#parse options
	try:
        opts,args = getopt.getopt(sys.argv[1:], "f:h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
       if o == '-f':
            USE_FILE = 1
            FILE = a
        else:
            usage(1)
	
	master(USE_FILE)