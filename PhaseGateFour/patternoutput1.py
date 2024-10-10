size = int(input("Enter size of your pattern : "))

for row in range(1, size+1):
 
	for column in range(1, row):

		if column % 2 == 0 :
			print("*", end = " ")
		
		if column % 2 != 0:
			print(column, end = " ")
		
	print(" ")