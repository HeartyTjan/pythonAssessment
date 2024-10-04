print("This are the even numbers : " , end = " ")
for number in range(1000,3001):

	first_digit = number //1000 % 10
	second_digit = number //100 % 10
	third_digit = number //10 % 10
	fourth_digit = number % 10

	if first_digit % 2 == 0 and second_digit % 2 ==0 and third_digit % 2 == 0 and fourth_digit % 2 == 0 :

		print(number, end = ",")



		
		