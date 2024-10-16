def swap(numbers)-> list:
	
	try:
		size = len(numbers)
	
		for index in range(1,size,2):

			temp = numbers[index]
			numbers[index] = numbers[index - 1]
			numbers[index-1] = temp
	except :
		raise ValueError("Invalid input")

	return numbers	


