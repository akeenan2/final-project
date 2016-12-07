#!/usr/bin/env python2.7
import sys
import getopt
import db # from db.py

def usage(status=0):
    print '''Usage: ./reducer.py [options]...

Options:
    -o          output the data
    -h          help'''
    sys.exit(status)

# words = dict of all key words to their frequency
def reducer(words):
    compiled_words = dict()
    for word in words:
        if word[0] in compiled_words:
            compiled_words[word[0]] += word[1]
        else:
            compiled_words[word[0]] = word[1]
    return compiled_words

# main execution
if __name__ == '__main__':
    print 'execute'