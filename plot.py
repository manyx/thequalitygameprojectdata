
#!/usr/bin/env python
from pylab import *
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
minTimings = {}
for entry in data["entries"]:
	if not int(entry["user"]) in y:
		newEntry = ( int(entry["user"]),userCount)
		userMapping.append(newEntry)
		userCount = userCount + 1
	try:
		if minTimings[int(entry["user"])] > float(entry["time"]):
			minTimings[int(entry["user"])] = float(entry["time"])		
	except KeyError:
		minTimings[int(entry["user"])] = float(entry["time"])
		
		
	y.append(int(entry["user"]))
	x.append(float(entry["time"]))
	
usersDict  = dict (userMapping)
usersDict2 = {}
minTimings2 = {}
userCount = len(userMapping)
for key, value in sorted(minTimings.iteritems(), key=lambda (k,v): (v,k)):
	usersDict2[key] = userCount
	userCount = userCount -1

newUsers = []
for usr in y:
	newUsers.append( usersDict2[usr])
minTime = min (x)
newTimes = []	
for aux in x:
	newTimes.append( float((aux - minTime)/1000/60/60/24))

x = newTimes
y = newUsers

N = 30


area = pi*(2.5 )**2 # 0 to 10 point radiuses
ylabel('Users')
xlabel('Time in days')

axis([min(x),max(x),min(y),max(y)])
c = scatter(x,y,s=area, marker='o', c='r')

show()

