#!/usr/bin/env python2.7
import sys
import getopt
from mapper import *
import db # from db.py

def usage(status=0):
    print '''Usage: python sort.py [options]...

Options:
    -u URL      url of website to analyze
    -s SORT     sorting algorithm [sort|quick|merge|bst]
    -f FILE     path to file used as input
    -o          output the data
    -h          help'''
    sys.exit(status)

# all sorting algorithms return a list of tuples (key word,count)
# uses built in sorting algorithm
def sort(words):
    return sorted(words.items(),key=lambda x:x[1])

# quick sort
def quick_help(words):
    #need to convert words dict to a list so we can sort it
    words_list = []
    for i in words:
        k = (i, words[i])
        words_list.append(k)
    sorted_list = quick(words_list)
    return sorted_list
# convert to a list
def quick(words_list):
    if len(words_list) == 0:
        return []
    else:
        pivot = words_list[0]
        lesser = quick([x for x in words_list[1:] if x[1] < pivot[1]])
        greater = quick([x for x in words_list[1:] if x[1] >= pivot[1]])
        return lesser + [pivot] + greater

# merge sort
def merge_help(words):
    # convert dict to a list
    words_list = []
    for i in words:
        k = (i, words[i])
        words_list.append(k)
    sorted_list = mergesort(words_list)
    return sorted_list
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def bst(words):
    
    global tuple_list
    #initializes the root of the tree
    root = Node(words[0], words[words[0]])

    # Constructs the tree
    for keys in words:
        bst_insert(root,Node(words[keys],words[words[keys]]))

    # Creates a tuple List in order
    in_order(root)

    return tuple_list

class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val 

def bst_insert(root,new_node):
    if root is None:
        root = new_node
    else:
        if root.val > new_node.val:
            if root.left is None:
                root.left = new_node
            else:
                bst_insert(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else:
                bst_insert(root.right, new_node)

tuple_list = []

def in_order(root):
    global tuple_list

    if not root:
        return

    in_order(root.left)
    tuple_list.append(root.key,root.value)
    in_order(root.right)


# default values
URL = ''
SORT = 'sort'
FILE = ''
WORDS = dict()
OUTPUT = False

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:s:f:oh")
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
        elif o == '-o':
            OUTPUT = True
        else:
            usage(1)

    # use a file as input
    if FILE != '':
        print FILE
        with open(FILE,'r+') as f:
            # build a dictionary from the file
            for line in f:
                l = line.split(' ')
                WORDS[l[0]] = l[1].rstrip()
            f.close()
    # if no url or url not in the db
    elif URL == '' or URL not in db.url_map:
        usage(1)
    # use a url as input, call mapper for the dict
    else:
        WORDS = mapper(URL)

    # run the chosen sorting algorithm
    if SORT == 'sort':
        sorted_words = sort(WORDS)
    elif SORT == 'quick':
        sorted_words = quick_help(WORDS)
    elif SORT == 'merge':
        sorted_words = merge_help(WORDS)
    elif SORT == 'bst':
        sorted_words = bst(WORDS)
    else:
        usage(1)

    # print results
    if OUTPUT:
        for word in sorted_words:
            print word[0] + ' ' + str(word[1])
