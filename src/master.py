#!/usr/bin/env python2.7
import sys
import time
from lxml import html
import requests
from collections import Counter
import getopt

import db
from mapper import mapper,lookup
from sort import sort

def usage(status=0):
    print '''Usage: ./master.py [options]...

Options:
    -n NUM      use NUM keywords in search (default 5)
    -l NUM      output NUM links (default 2)

    -g          google search on keywords (default custom-built search)

    -o          output all keywords found with their counts
    -t          print the top words with their counts
    -d          disable the search for headlines

    -h          help'''
    sys.exit(status)

def search(keywords):
    url = "https://news.google.com/#q="
    for word in keywords[:-1]:
        url = url + word[0] + '+'
    url = url + keywords[-1][0]

    # fetch the search result page
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # get the google search output
    headlines = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/span/text()")
    links = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/@href")
    
    # return the list of headlines
    return zip(headlines,links)

def master(urls):
    keywords = Counter()
    # call mapper on all urls and reduce to one master dict
    for url in urls:
        temp_dict = Counter(mapper(url))
        keywords = keywords + temp_dict
    # sort by count and return
    return sort(keywords)

NUM_KEYWORDS = 5
NUM_LINKS = 2
GOOGLE = False
OUTPUT = False
TOP = False
DISABLE = False

# main execution
if __name__ == '__main__':
    # parse options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "n:l:gotdh")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-n':
            NUM_KEYWORDS = int(a)
        elif o == '-l':
            NUM_LINKS = int(a)
        elif o =='-g':
            GOOGLE = True
        elif o == '-o':
            OUTPUT = True
        elif o == '-t':
            TOP = True
        elif o == '-d':
            DISABLE = True
        else:
            usage(1)

    # call master function
    words = master(db.urls)

    # print results (all keywords + counts)
    if OUTPUT:
        for word in words:
            print word[0] + ' ' + str(word[1])

    # pull out most frequent words
    if TOP:
        for word in words[:-1*(NUM_KEYWORDS+1):-1]:
            print word[0] + ' ' + str(word[1])

    if not DISABLE:
        # use google search
        if GOOGLE:
            headlines = search(words[:-1*(NUM_KEYWORDS+1):-1])
            # print the top headlines
            for headline in headlines[:NUM_LINKS]:
                print headline[0]
                print headline[1]
                print '\n',
        # use our own search/weighting algorithm
        else:
            headlines = []
            # compile list of all headlines from sources with matches to keywords
            for url in db.urls:
                # call the algorithm (in mapper.py)
                headlines += lookup(url,words[:-1*(NUM_KEYWORDS+1):-1])
            # sort by matches and then by weight
            headlines.sort(key=lambda element: (element[0], element[1]))
            # print the top headlines
            for headline in headlines[:-1*(NUM_LINKS+1):-1]:
                print headline[2]
                print headline[3]
                print '\n',
