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
    sorted = quick(words_list)
    return sorted
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
    sorted = mergesort(words_list)
    return sorted
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

    # if no url or url not in the db
    if URL == '' or URL not in db.url_map:
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
    else:
        WORDS = mapper(URL)

    #print WORDS
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
    for word in sorted_words:
        print word[0] + ' ' + str(word[1])