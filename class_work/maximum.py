def maximum(first_input, second_input, third_input) :
	largest = 0
	
	if first_input> largest :
		largest = first_input

	if second_input > largest :
		largest = second_input

	if third_input > largest :
		largest = third_input

	return largest


def minimum(first_input, second_input, third_input) :

	smallest = 0

	if first_input < second_input :
		smallest = first_input
	else:
		smallest = second_input

	if third_input <  smallest :
		smallest = third_input
	
	return smallest
	



print(maximum(-10,100,70))
print(minimum(09,0,-15))