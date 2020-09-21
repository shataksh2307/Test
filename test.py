rawstr = input("Enter a number: ")
try:
	ival = int(rawstr)
	
except:
	ival = -1
	
if ival > 0:
	print("Great Work")
else:
	print("Not a number")
