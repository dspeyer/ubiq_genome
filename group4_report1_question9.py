#!/usr/bin/python
###########################################################################
# Number 9
# Plot the pace of the strand sequencing for 2D reads classified as failed vs passed.
#
# cvs file of time data created with the following poretools command lines:
# 
#  $ poretools times pass/has2d/ >/Users/annebozack/Documents/genomics/timesPass.txt
#  $ poretools times fail/has2d/ >/Users/annebozack/Documents/genomics/timesFail.txt
###########################################################################

import sys
import os
import csv
import warnings


warnings.simplefilter("ignore")

path=sys.argv[1]

os.system('poretools times '+path+'downloads/pass/ >'+path+'downloads/pass/timesPass.txt')
os.system('poretools times '+path+'downloads/fail/has2d/ >'+path+'downloads/fail/has2d/timesPass.txt')

# For passed
with open(''+path+'downloads/pass/timesPass.txt') as times_readP: 
	reader = csv.reader(times_readP, delimiter='\t') 
	timesPass = list(reader)

lengthsPass = []
lengthsIntPass = []

for i in range(1, len(timesPass)):
	lengthIntPass = int(timesPass[i][2])
	lengthsPass.append(lengthIntPass)

durationPass = []
durationIntPass = []

for i in range(1, len(timesPass)):
	durationIntPass = int(timesPass[i][5])
	durationPass.append(durationIntPass)

# For failed
with open(''+path+'downloads/fail/has2d/timesPass.txt') as times_readF: 
	reader = csv.reader(times_readF, delimiter='\t') 
	timesFail = list(reader)

lengthsFail = []
lengthsIntFail = []

for i in range(1, len(timesFail)):
	lengthIntFail = int(timesFail[i][2])
	lengthsFail.append(lengthIntFail)

durationFail = []
durationIntFail = []

for i in range(1, len(timesFail)):
	durationIntFail = int(timesFail[i][5])
	durationFail.append(durationIntFail)

# Plotting
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axis([-50, 800, -500, 15000])
ax.scatter(durationPass, lengthsPass, c='red', alpha=0.2, label='Pass')
ax.scatter(durationFail, lengthsFail, c='blue', alpha=0.05, label='Fail')
plt.legend(loc='upper right', numpoints=1)
fig.suptitle('Sequence length by duration in pore, sec')
plt.xlabel('Duration in pore, sec')
plt.ylabel('Length of sequence')
plt.savefig('q9.png')


