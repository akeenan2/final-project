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

def master():
	master_dict = Counter()

	with open(FILE,'r+') as f:
        # build a dictionary from the file
        for line in f:
            l = line.split(' ')
            WORDS[l[0]] = l[1].rstrip()
        f.close()

	# urls 
	for url in db.urls:
		temp_dict = Counter(mapper(url))
		master_dict = master_dict + temp_dict
		
	master_dict = reducer(master_dict)
	master_dict = sort(master_dict)
	
	time.sleep(10)

# main execution
if __name__ == '__main__':

	while True:
		master()