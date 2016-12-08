#!/usr/bin/env python2.7
import sys
import getopt
from mapper import *
import db # from db.py

tuple_list = []
sys.setrecursionlimit(3000)

# all sorting algorithms return a list of tuples (key word,count)
def sort(words,sort_type=''):
    if sort_type == "quick":
        return quick_help(words)
    elif sort_type == "merge":
        return merge_help(words)
    elif sort_type == "bst":
        return bst(words)
    else: # use default
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
    key, value = words.popitem()
    root = Node(key, value)

    # Constructs the tree
    items = len(words)
    for i in range(items):
        key, value = words.popitem()
        bst_insert(root,Node(key,value))

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

def in_order(root):
    global tuple_list

    if not root:
        return

    in_order(root.left)
    tuple_list.append((root.key,root.val))
    in_order(root.right)
