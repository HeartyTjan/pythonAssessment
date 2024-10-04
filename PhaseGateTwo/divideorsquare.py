import math

def divide_or_square(number):

	if not isinstance(number, int):
		
		raise ValueError ("Enter Valid number")
	
	if number <= 0 :
		
		raise ValueError ("Enter Valid number")
		
	if number % 5 == 0 :

		return round(math.sqrt(number),2)
	
	else :
		return number / 5

	


