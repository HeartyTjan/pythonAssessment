def get_largest(array):

	if not isinstance(array, (list)):
		raise TypeError("array not a list")
	
	largest = array[0]

	for number in range(len(array)) :
		
		if array[number] > largest :
	        	largest = array[number]	
	 
	return largest


def get_reverse(array):

	size = len(array)
	count = 0
	reverse = size - 1

	while count < reverse :
		temp = array[count]
		array[count] = array[reverse]
		array[reverse] = temp

		count +=1
		reverse -= 1
	
	return array

def get_reverse_list(array):

	size = len(scores)
	reverse_list = []

	for index in range(size-1,-1,-1):

		reverse_list += [array[index]]
	
	return reverse_list


def check_element(array,number):
	if not isinstance(array, list):	
		raise TypeError("invalid input, Enter list type")
	
	size = len(array)

	for count in range(size):
		
		if number == array[count]:
			 return True
		else :
			return False

def print_odd_positions(list):
	
	try:	
		odd_list = []
		count = 0
		for odd in list:
			if count % 2 == 1:
				odd_list += [odd]
			count +=1
	except:
		raise TypeError ("Invalid Type. Enter a list")

	return odd_list

def print_even_positions(user_list):

	if not isinstance(user_list, list):
		raise TypeError("invalid input")
		
	even_list = []
	count = 0
	for even in user_list:
		if count % 2 == 0:
			even_list += [even]
		count +=1

	return even_list

def string_is_palindrome(user_list):	
	if not isinstance(user_list, list):
		raise TypeError ("Invalid Type. Enter a list")

	size = len(user_list)

	reverse_list = []

	for index in range(size-1,-1,-1):

		reverse_list += [user_list[index]]
	
	if user_list == reverse_list:
		return True
	else:



def concatinate_list(user_list, user_list2):
	
	if not isinstance(user_list,list) or not isinstance(user_list2, list):
		raise TypeError ("Type list argument required")

	if isinstance(user_list, str) or isinstance(user_list2, str):
		raise TypeError("invalid string not required")
	
	if not isinstance(user_list,list) and not isinstance(user_list2, list):
		raise TypeError ("Type list argument required")
	
	concat = user_list + user_list2
	
	return concat
	



