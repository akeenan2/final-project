#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from master import master
from mapper import lookup

def usage(status=0):
    print '''Usage: ./lookup_test.py'''
    sys.exit(status)

# main execution
if __name__ == '__main__':
    # parse options
    try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        usage(1)

    urls = [
        "http://michaelsills.com/sample_links.html",
        "http://michaelsills.com/sample_links_2.html"
    ]

    # call master with demo urls
    keywords = master(urls)

    # call lookup with keywords
    headlines = []
    for url in urls:
        headlines += lookup(url,keywords)

    # sort by matches then by weight
    headlines.sort(key=lambda element: (element[0], element[1]))

    # print top two headlines
    for headline in headlines[:-2:-1]:
        print headline[2]
        print headline[3]
        print '\n',
    print headlines[-2][2]
    print headlines[-2][3]
