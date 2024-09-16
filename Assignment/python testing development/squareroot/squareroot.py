import math
def get_squareroot(number):
	if number < 0 :
		raise ValueError("Invalid input. Enter valid input")
	if not isinstance(number, int):
		raise TypeError("Input must be integer")

	if number % 5 == 0 :
		return round(math.sqrt(number),2)
	else :
		return number 