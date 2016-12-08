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
    -o          output data to stdout
    -n NUM      generate NUM keywords
    -d          disable the search for headlines
    -t          print the top words
    -h          help'''
    sys.exit(status)

def search(keywords):
    url = "https://news.google.com/#q="
    for word in keywords[:-1]:
        url = url + word[0] + '+'
    url = url + word[0]
    # fetch the website
    page = requests.get(url)
    tree = html.fromstring(page.content)

    headlines = []
    links = []

    headline = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/span/text()")
    link = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/@href")
    for i in range(10):
        print headline[i]
        print link[i]

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
NUM = 5
DISABLE = False
TOP = False

# main execution
if __name__ == '__main__':
    # parse options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "on:dth")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-o':
            OUTPUT = True
        elif o == '-n':
            NUM = int(a)
        elif o == '-d':
            DISABLE = True
        elif o == '-t':
            TOP = True
        else:
            usage(1)

    # call master function
    words = master(db.urls)

    # print results
    if OUTPUT:
        for word in words:
            print word[0] + ' ' + str(word[1])

    # pull out most frequent words
    trending = words[:-1*(NUM+1):-1]
    if TOP:
        for word in trending:
            print word[0] + ' ' + str(word[1])
    if not DISABLE:
        search(trending)
