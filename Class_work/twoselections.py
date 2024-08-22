user_input = int(input("Enter your score: "))

if user_input > 100:
	print("Invalid Number")

elif user_input >= 75 and user_input <= 100:
	print("Excellent!")

elif user_input >= 65 and user_input < 75:
	print("Great!")

elif user_input >= 50 and user_input < 65:
	print("very Good!")

elif user_input >= 40 and user_input < 49:
	print("good!")

elif user_input >= 30 and user_input < 0:
	print("fail!")

else: 
	print("Try again next year!!")

