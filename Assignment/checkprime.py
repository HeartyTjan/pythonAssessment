def is_prime(number) :

	factor = 0
	
	for count in range(1, number+1) :

		if number % count == 0 :
			 factor = factor + 1

	if factor == 2:

		return "It is a prime number"
	else :
		return "Not a prime number"
