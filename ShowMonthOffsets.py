#!/bin/python 

"""

Create list of numbers, offsets (sum of days in preceding months) for each month. 

e.g. Jan=0, Feb=31, Mar=59, etc. 

"""

monthLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

currTotal = 0
monthNum = 0
for currMonth in monthLen: 
	currTotal = currTotal + currMonth
	monthNum = monthNum + 1
	print(f"{monthNum} = {currTotal}")

