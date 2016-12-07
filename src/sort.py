#!/usr/bin/env python2.7
import sys
from mapper import *
import getopt

def usage(status=0):
    print '''Usage: python sort.py [options]...

Options:
    -u URL      url of website to analyze
    -s SORT     sorting algorithm [sort|quick|merge|bst]
    -f FILE     path to file used as input
    -h          help'''
    sys.exit(status)

# all sorting algorithms return a list of tuples (key word,count)
# uses built in sorting algorithm
def sort(words):
    return sorted(words.items(),key=lambda x:x[1])

# quick sort
def quick_help(words):
    quick(words.items, 0)
#words is now a list not a dict
def quick(words_list, index):
    if len(words_list) == 0:
        return []
    else:
        pivot = words_list[0]
        lesser = quick([x for x in words_list[1:] if x[index] < pivot[index]], index)
        greater = quick([x for x in words_list[1:] if x[index] >= pivot[index]], index)
        return lesser + [pivot] + greater

# merge sort
def merge(words):
    return words

# binary tree/bst
def bst(words):
    return words

# default values
URL = ''
SORT = 'sort'
FILE = ''
WORDS = dict()

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:s:f:h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-u':
            URL = a
        elif o == '-s':
            SORT = a
        elif o == '-f':
            FILE = a
        else:
            usage(1)

    # use a file as input
    if FILE != '':
        with open(FILE,'rb') as f:
            # build a dictionary from the file
            for line in f:
                l = line.split(' ')
                WORDS[l[0]] = WORDS[l[1]]
            f.close()
    # use a url as input, call mapper for the dict
    elif URL != '':
        WORDS = mapper(URL)
    else:
        usage(1)
    # run the chosen sorting algorithm
    if SORT == 'sort':
        sorted_words = sort(WORDS)
    elif SORT == 'quick':
        sorted_words = quick_help(WORDS)
    elif SORT == 'merge':
        sorted_words = merge(WORDS)
    elif SORT == 'bst':
        sorted_words = bst(WORDS)
    else:
        usage(1)
    # print results
    for word in sorted_words:
        print word[0] + ' ' + str(word[1])
