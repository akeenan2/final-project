#!/usr/bin/env python2.7
import time
from collections import Counter
import db

while True:
	masterDict = Counter()
	# urls 
	for url in db.urls:
		dict = Counter(mapper(url))
		masterDict = masterDict + dict
		
	masterDict = reduce(masterDict)
	masterDict = sort(masterDict)
	
	
	time.sleep(10)

