def get_square(number) :

	if not isinstance(number, (int,float)):
		raise ValueError ("Invalid Input")
	
	product = 1
	
	for count in range(2):
		
		product = round(product * number,2)

	return product

def get_array_square(list) :

	for element in list:

		if not isinstance(element, (int,float)):

			raise ValueError ("List has a String value")
	
	size = len(list)
	squared_array = []

	for count in range(size):
		
		square = get_square(list[count])
		squared_array.append(square)

	return squared_array

def sort_array(list):

	for element in list:

		if not isinstance(element, (int,float)):

			raise ValueError ("List has a String value")

	size = len(list)
	minimum = 0
	sorted_array = []

	for count in range(size):
	
		minimum = count
		
		for compared_number in range(count+1,size):

			if list[compared_number] < list[minimum]:

				minimum = compared_number
	
		temp = list[minimum]
		list[minimum] = list[count]
		list[count] = temp

	return list
		

