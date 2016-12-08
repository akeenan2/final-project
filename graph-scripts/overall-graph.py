#!/usr/bin/env python2.7
import matplotlib.pyplot as plt
import numpy as np

# data to plot
sorts = ('default','quick','merge','bst')
n_groups = 4
times = (21.595594,26.316448,22.678596,27.567272)
memory = (23.51468752,24.2783594,23.58570304,23.9197656)
 
# create plot
fig = plt.figure()
ax = plt.subplot(111)
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
plt.bar(index, times, bar_width,
     alpha=opacity,
     color='#36e5cf',
     label='time (cs)')
 
plt.bar(index + bar_width, memory, bar_width,
     alpha=opacity,
     color='#ff5066',
     label='memory (Mb)')

# set legend
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# add labels
plt.xlabel('Sort')
plt.ylabel('Measurement')
plt.title('Time/Memory Usage of Sorting Algorithms')
plt.xticks(index + bar_width,sorts)
plt.savefig('graphs/overall.png')
plt.show()
