def get_reverse(number):

	reverse = 0

	while number != 0 :

		reverse = reverse * 10 + number % 10

		number = number // 10
	
	return reverse


def check_for_palindrome(number):

	reversed_number = get_reverse(number)
	
	if number == reversed_number:
		return True

	else :
		return False

	

	

