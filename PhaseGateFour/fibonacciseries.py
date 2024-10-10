def fibonacci_series(number):

	if not isinstance(number, int):

		raise ValueError("Enter valid input")
	
	if number < 0:

		raise ValueError ("Invald input")

	first_number = 0
	second_number = 1
	next_number = 0
	print("Fibonacci series : ")

	for count in range(number):
		
	 	if count > 1 :
		
		 	next_number = first_number + second_number

		 	first_number = second_number
		 	second_number = next_number

		 	print(second_number, end = " ")
		 	

	 	else :
	 		print(count, end = " ")


number = int(input("Enter a number : "))
fibonacci_series(number)