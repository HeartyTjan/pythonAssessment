def get_product(number, second_number) :
	
	if isinstance(second_number, float):
		temp = second_number
		second_number = number
		number = temp
		
	if not isinstance(number ,(int,float)):
		raise ValueError ("Invalid input")

	if not isinstance(second_number ,(int,float)):
		raise ValueError ("Invalid input")

	if not isinstance(number,(int,float)) or not isinstance(second_number,(int,float)):
		raise ValueError ("Invalid input")

	
	if number < 0 and second_number < 0 :
		number = - number
		second_number = -second_number
		
	if second_number < 0 :
		temp = second_number
		second_number = number
		number = temp

	if isinstance(number, float): #and isinstance(second_number, float):

		converted_number = int(number)
		number = converted_number
		
		converted_second_number = int(second_number)
		second_number = converted_second_number
	
	
		
	product = 0

	for count in range(second_number):
		product += number 
	
	return product	
	

	

print(get_product(2.2,4.2))	
