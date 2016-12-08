#!/usr/bin/env python2.7
import os
import sys
sys.path.insert(0,'../src')
import db

SORTS = ['default','quick','merge','bst']

with open('benchmark.txt','r') as f:
    for line in f:
        l = line.strip.split('\t')