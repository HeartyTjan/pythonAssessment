def add_string_integer(first_integer, second_integer):

	first_integer_in_number = int(first_integer)
	second_integer_in_number = int(second_integer)

	total =  first_integer_in_number + second_integer_in_number
	
	total_string = str(total)

	return total_string


print(add_string_integer("6","3"))	