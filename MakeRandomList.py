import random
"""This creates and returns a list of numbers in range start-end of length num"""

def Rand(start, end, num):
	res = []
	for j in range(num):
		res.append(random.randint(start,end))
	return res