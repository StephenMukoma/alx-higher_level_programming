#!/usr/bin/python3
num1 = 0
num2 = 0
for num1 in range(0,10):
	for num2 in range(0,10):
		if num1 > num2 or num1 == num2:
			pass			
		else:
			print("{}{}".format(num1,num2), end=', ')
			print("", end="")
