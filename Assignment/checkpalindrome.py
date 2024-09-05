def is_palindrome(number) :
	original_number = number
	reverse = 0

	while(number != 0) :

		reverse = reverse * 10 + number % 10
		number = number // 10
	
	if original_number == reverse :
		return "its a palindrome" 
	else :
		return "its not palindrome"
