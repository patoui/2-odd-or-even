num = raw_input("Number to check: ")
check = raw_input("Number to divide by: ")
isEven = True if int(num) % int(check) == 0 else False
isFourEven = True if int(num) % 4 == 0 else False
output = check + " does not go into " + num + " evenly"
if (isEven):
	output = check + " does into " + num + " evenly"
print(output)
if (isFourEven):
	print(num + " is a multiple of 4")
