
print("""
	Calculate Sum of Multiple of 10
	-------------------------------
	"""
	)

sum_total = 0
for number in range(1,20001) :
	
	if number % 10 == 0 :

		sum_total = sum_total + number

print("The sum of multiple of 10 is :" , sum_total)
