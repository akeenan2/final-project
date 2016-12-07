#!/usr/bin/env python2.7
import sys
import getopt
import db

def usage(status=0):
    print '''Usage: ./reducer.py [options]...

Options:
    -o          output the data
    -h          help'''
    sys.exit(status)

# words = dict of all key words to their frequency
def reducer(words):
    compiled_words = dict()
    for word,count in words.iteritems():
        if word in compiled_words:
            compiled_words[word] += count
        else:
            compiled_words[word] = count
    return compiled_words

# main execution
if __name__ == '__main__':
    print 'execute'