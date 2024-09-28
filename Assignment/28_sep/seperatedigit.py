
def seperate_digit_v2(digit):

	digit_list = str(digit)

	sep_list = ' '

	for number in digit_list:

		sep_list += number

		sep_list += "  "

	return sep_list
 



digit = int(input("Enter digit : "))

digit_list = str(digit)

if len(digit_list) == 9:
	div = 100000000
elif len(digit_list) == 8:
	div = 10000000
elif len(digit_list) == 7:
	div = 1000000
elif len(digit_list) == 6:
	div = 100000
elif len(digit_list) == 5:
	div = 10000
elif len(digit_list) == 4:
	div = 1000
elif len(digit_list) == 3:
	div = 100
elif len(digit_list) == 2:
	div = 10

print("Seperated digit is :", end = " ")
for number in range(len(digit_list)):
	
	sep = digit // div % 10

	print(f"{round(sep)} ", end = " ")
		
	div /= 10 	

