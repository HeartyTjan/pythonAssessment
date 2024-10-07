import random
correct_count = 0

for count in range(10):
	first_number = random.randrange(1,100)
	second_number = random.randrange(1,100)

	if first_number < second_number :
	
		answer = int(input(f"What is {second_number} - {first_number} : "))
		
		result = second_number - first_number
	else : 
		answer = int(input(f"What is {first_number} - {second_number} : "))

		result = first_number - second_number 

	if(answer == result):
		print("Correct response")
		correct_count += 1
	else :  
		print("incorrect response")
		
	
print()

print(f"Your final score is {correct_count}")
