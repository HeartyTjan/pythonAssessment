def display_pattern(number) :

	for row in range(number,1,-1) :
		for column in range( number, row, -1):
			print(" ")

		for number1 in range(1, row,):
			print(number1, end = " ")







line_number = int(input("Enter the number of lines : "))

display_pattern(line_number)		
		

"""
for number in range(1,number):
	
		print(" ")
	
		for count in range(1, number):
		
			print(count, end = " ")


for number1 in range(number, number-1) :
		
		print(" ")

		for counter in range(number1, 1, -1) :

			print(counter, end = " ")

"""