import random

print("""

	Sum Of Two Random Number
       ===========================

""")

first_number = random.randrange(100)
second_number = random.randrange(100)

user_answer = 0;
result = 1;

while(user_answer != result):

	user_answer = float(input(f"What is {first_number} + {second_number} : "))
	print()

	result = first_number + second_number

	if(user_answer == result):
	
		print("Correct Answer")
	else :
		print("incorrect Answer")
