import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import time
import json
from pprint import pprint

json_data=open('out.txt')

data = json.load(json_data)

json_data.close()

x = []
y = []

userCount = 0
userMapping = []
for entry in data["entries"]:
	if not int(entry["user"]) in y:
		newEntry = ( int(entry["user"]),userCount)
		userMapping.append(newEntry)
		userCount = userCount + 1
	y.append(int(entry["user"]))
	x.append(long(entry["time"]))
	
usersDict  = dict (userMapping)

newUsers = []
for usr in y:
	newUsers.append( usersDict[usr])
minTime = min (x)

newTimes = []	
for aux in x:
	newTimes.append( int((aux - minTime)/1000/60))

x = np.array(newTimes)
y = np.array(newUsers)

x2 = np.random.randn(1000)
y2 = np.random.randn(1000)

"""
with open('test.txt', 'w') as f2:
	read_data = f2.write(repr(x4))
	read_data = f2.write(repr(y4))
	read_data = f2.write(repr(x))
	read_data = f2.write(repr(y))
	f2.closed
"""

print type(x)
print type(x2)

nullfmt   = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left+width+0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(40,40))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y)

# now determine nice limits by hand:
binwidth = 1000
xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
lim = ( int(xymax/binwidth) + 1) * binwidth

#axScatter.set_xlim( (0, lim) )
#axScatter.set_ylim( (0, lim) )
import pdb;pdb.set_trace()
bins = np.arange(0, lim + binwidth, binwidth)
axHistx.hist(x, bins=bins)
axHisty.hist(y, bins=bins, orientation='horizontal')

axHistx.set_xlim( axScatter.get_xlim() )
axHisty.set_ylim( axScatter.get_ylim() )

plt.show()