#!/usr/bin/env python2.7
import matplotlib.pyplot as plt
import numpy as np

# data to plot
words = []
counts = []
with open('graph-scripts/top-words.txt','r') as f:
    for line in f:
        l = line.rstrip().split(' ')
        words.append(l[0])
        counts.append(int(l[1]))

words = np.array(words)
counts = np.array(counts)

# create plot
y_pos = np.arange(len(words))
plt.barh(y_pos,counts,align='center',alpha=0.5,color="#ff5066")
plt.yticks(y_pos,words)

# add labels
plt.xlabel('Key Word')
plt.ylabel('Word Count')
plt.title('Top Key Words')
plt.savefig('graphs/top-words.png')
plt.show()
