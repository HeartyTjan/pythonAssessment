def descending_order(lst_numbers):

	for element in lst_numbers:
		
		if not isinstance(element,int):
			raise ValueError ("Invalid input")
	
	size = len(lst_numbers)
	
	for index in range(size):
		
		for count in range(size):

			if lst_numbers[count] < lst_numbers[index]:
				temp = lst_numbers[count]
				lst_numbers[count] = lst_numbers[index]
				lst_numbers[index]=temp

	return lst_numbers

#print(descending_order([5,2,7,1,8,2]))	

def ascending_order(lst_numbers):
	
	try:		
		size = len(lst_numbers)
		
		for index in range(size):
		
			for count in range(size):

				if lst_numbers[count] > lst_numbers[index]:
					temp = lst_numbers[count]
					lst_numbers[count] = lst_numbers[index]
					lst_numbers[index]= temp
	except:
		raise ValueError ("Invalid input")
		
	return lst_numbers

def multiply_third_index(lst_numbers):

	size = len(lst_numbers)
	product = 1
	for index in range(2, size, 3):
		product *= lst_numbers[index]

	return product

#print(ascending_order([5,2,7,9,8,2]))	
#print(descending_order([5,2,7,"de",8,2]))	

