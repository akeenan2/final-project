#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'src')
import getopt
from mapper import mapper
import db

def usage(status=0):
    print '''Usage: ./sort_test.py'''
    sys.exit(status)

# default values
SORTS = [
    'default',
    'quick',
    'merge',
    'bst'
]
OUTPUT = False
TEST_URLS = {
    "sample_links":"http://michaelsills.com/sample_links.html",
    "sample_links_2":"http://michaelsills.com/sample_links_2.html"
}
# main execution
if __name__ == '__main__':
    # user input
    try:
        opts,args = getopt.getopt(sys.argv[1:], "h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        usage(1)

    # generate files
    for sort in SORTS:
        for name,url in TEST_URLS.iteritems():
            # run the sort script
            os.system("./test/run_sort.py -u {} -s {} -o > data/{}_{}_test.txt".format(url,sort,sort,name))

    # check sort
    for sort in SORTS:
        for name,url in TEST_URLS.iteritems():
            os.system("./test/check_sort.py -f data/{}_{}_test.txt".format(sort,name))
