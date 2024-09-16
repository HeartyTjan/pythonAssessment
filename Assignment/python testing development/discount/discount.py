def my_discount(price, discount):
	if price < 0 or discount < 0 :
		raise ValueError ("Invalid input")
	
	if not isinstance (discount, int) :
		raise TypeError("Input must be integer")

	discount_in_decimal =  discount / 100
	return price - (price * discount_in_decimal)