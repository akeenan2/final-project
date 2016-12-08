#!/usr/bin/env python2.7
import sys
import time
from collections import Counter
import db
from mapper import mapper
from sort import sort
import getopt
from lxml import html
import requests

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
	-u URLS     list of urls 
    -o          output data to stdout
    -p          print counts of top ten if set
    -h          help'''
    sys.exit(status)

def search(keywords):
    url = "https://news.google.com/#q="
    for word in keywords[:-1]:
        url = url + word + '+'
    url = url + word
    # fetch the website
    page = requests.get(url)
    tree = html.fromstring(page.content)

    headlines = []
    links = []

    headline = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/span/text()")
    link = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/@href")

    print headline[0]
    print link[0]

def master(urls):
    master = Counter()
    # call mapper on all urls and reduce to one master dict
    for url in urls:
        temp_dict = Counter(mapper(url))
        master = master + temp_dict
    # sort by count
    master = sort(master)
    return master

OUTPUT = False
PRINT = False
# main execution
if __name__ == '__main__':
    # parse options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "oph")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-o':
            OUTPUT = True
        elif o == '-p':
        	PRINT = True
        else:
            usage(1)
    # call master function

    words = master(db.urls)
    # print results
    if OUTPUT:
        for word in words:
            print word[0] + ' ' + str(word[1])
    # pull out top 10 most frequent words
    #print "Top Words:"
    trending = words[:-6:-1]
    for word in trending:
    	if PRINT:
    		print word[0] + ' ' + str(word[1])
    	else:
    		print word[0]
    