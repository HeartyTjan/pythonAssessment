def display_sorted_number(num1,num2,num3) :
	sum = num1 + num2 + num3
	
	highest = num1
	smallest = num1

	if (num2 > num1) :
		highest = num2

	if (num3 > highest) :
		highest = num3
	
	high = sum - highest - smallest

	print(" {} {} {}" .format(highest, high, smallest))