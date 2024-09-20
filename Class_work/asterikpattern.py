userInput = int(input("Enter number of size :"))

for row in range(0,userInput+1):
	print(" ")

	for column in range(0, row):
		print("*",end = " ")
		