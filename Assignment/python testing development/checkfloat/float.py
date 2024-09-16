def only_float(first_number, second_number):
	if isinstance(first_number,float) and isinstance(second_number,float) :
		return 2

	if isinstance(first_number,float) and not isinstance(second_number,float) :
		return 1
	if not isinstance(first_number,float) and not isinstance(second_number,float) :
		return 0




