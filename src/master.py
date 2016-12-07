import time
from collections import Counter

while True:

	masterDict = Counter()
	
	for url in urls:
		dict = Counter(mapper(url))
		masterDict = masterDict + dict
		
	masterDict = reduce(masterDict)
	masterDict = sort(masterDict)
	
	
	time.sleep(10)

