###########################################################################
# Number 9
# Plot the pace of the strand sequencing for 2D reads classified as failed vs passed.
#
# cvs file of time data created with the following poretools command lines:
# 
#  $ poretools times pass/has2d/ >/Users/annebozack/Documents/genomics/timesPass.txt
#  $ poretools times fail/has2d/ >/Users/annebozack/Documents/genomics/timesFail.txt
###########################################################################

# For passed
import csv

with open('/Users/annebozack/Documents/genomics/timesPass.txt') as times_readP: 
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
with open('/Users/annebozack/Documents/genomics/timesFail.txt') as times_readF: 
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
ax.axis([-100, 1000, -500, 15000])
ax.scatter(durationPass, lengthsPass, c='red', alpha=0.2, label='Pass')
ax.scatter(durationFail, lengthsFail, c='blue', alpha=0.05, label='Fail')
plt.legend(loc='upper right', numpoints=1)
fig.suptitle('Sequence length by duration in pore, sec')
plt.xlabel('Duration in pore')
plt.ylabel('Length of sequence')
plt.show()


