#!/usr/bin/env python2.7
import matplotlib.pyplot as plt
import numpy as np

sorts = ('default','quick','merge','bst')
sizes = (125,174,256,268,400,470,492,502,528,1708)
colors = ('#ef3cc7','#36e5cf','#cd6df3','#0cde70')

all_benches = []
#with open('graph-scripts/bench-memory.txt','r') as f:
with open('graph-scripts/bench-time.txt','r') as f:
    bench = [] # store either the array of memory or times
    count = 0
    for line in f:
        l = float(line.rstrip())
        if count < 10:
            bench.append(l)
            count += 1
        if count == 10:
            all_times.append(np.array(bench))
            count = 0
            bench = []

fig = plt.figure()
ax = plt.subplot(111)

i = 0
for bench in all_benches:
    plt.plot(sizes,bench,label=sorts[i],color=colors[i])
    i+=1

# set legend
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.xlabel('Length of File (lines)')
plt.ylabel('Execution Time (seconds)')
plt.title('Time to Execute of Sorting Algorithms')
#plt.savefig('graphs/memory.png')
plt.savefig('graphs/times.png')
plt.show()
