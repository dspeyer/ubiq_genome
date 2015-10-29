###########################################################################
# Number 8
# Plot the obtained sequence length over time for 2D reads.
#
# cvs file of time data created with the following poretools command lines:
# 
#  $ poretools times pass/has2d/ >/Users/annebozack/Documents/genomics/timesPass.txt
###########################################################################

import csv

with open('/Users/annebozack/Documents/genomics/timesPass.txt') as times_readP: 
	reader = csv.reader(times_readP, delimiter='\t') 
	timesPass = list(reader)

lengths = []
lengthsInt = []

for i in range(1, len(timesPass)):
	lengthInt = int(timesPass[i][2])
	lengths.append(lengthInt)

timeStart = []
timeIntStart = []

for i in range(1, len(timesPass)):
	timeIntStart = int(timesPass[i][4])
	timeStart.append(timeIntStart)

# Minimum time = 1445624726
timePassed = []
dif = 0

for i in range(0, len(timeStart)):
	dif = (timeStart[i] - 1445624726)/60
	timePassed.append(dif)

# Plotting
import matplotlib.pyplot as plt

txt = '''
	This graph was generated from the 2D pass reads, and time was calculated as time (in minutes)
	that each read was initiated from the time the first read was initiated.  Those reads that
	initiated late did not achieve a long read length.'''

fig, ax = plt.subplots()
ax.axis([-100, 2000, -500, 15000])
ax.scatter(timePassed, lengths, c='red', alpha=0.2)
fig.suptitle('Sequence length by time entered pore')
plt.xlabel('Time after first read initiated, min')
plt.ylabel('Length of sequence')
fig = plt.gcf()
fig.subplots_adjust(bottom=0.21)
fig.text(.03,.03,txt)
plt.show()

