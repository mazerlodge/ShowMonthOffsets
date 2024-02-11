#!/bin/python 

"""
OUtput list of length of month for each month. 

e.g. [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

"""

# used for validation
validateMonthLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getLengthOfMonth(monthNum):
	# Return length of the month specified, e.g. given 1 return 31.
	
	monthLen = -1

	if (monthNum < 8): 
		# January through July
		if (monthNum % 2 == 0): 
			# even 
			if (monthNum == 2): 
				monthLen = 28
			else: 
				monthLen = 30
		else:
			# odd 
			monthLen = 31
			
	else: 
		# August through December
		if (monthNum % 2 == 0): 
			# even
			monthLen = 31
		else:
			# odd 
			monthLen = 30
		
	return(monthLen)


for monthNum in range(1,13): 
	monthLen = getLengthOfMonth(monthNum)
	print(f"month {monthNum} has {monthLen} days")
	