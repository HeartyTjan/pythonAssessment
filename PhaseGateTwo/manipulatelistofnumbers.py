import random

def get_random():

	numbers = []

	for count in range(0,10):

		generated_random = random.randint(1,50)
	
		numbers.append(generated_random)

	return numbers

def get_len(list_of_numbers):
	
	list_count = 0

	for number in list(list_of_numbers):

		list_count += 1

	return list_count
	

numbers = get_random()

print("List of 10 numbers : ", numbers)


size = get_len(numbers)

total_even = 0
total_odd = 0
product = 1
counter = 1
total_element = 0

for count in range(size) :

	total_element += numbers[count] 

	if count % 2 == 0:
		
		total_even  += numbers[count]

	else:
		total_odd  += numbers[count]

	if counter % 3 == 0 :

		product *= numbers[count]
			
	counter += 1



average = round(total_element / count,2)		
		
print("Total of numbers at even position : ", total_even)
print("Total of numbers at odd position : ", total_odd)
print("Product of numbers  in third Position : ", product)
print("The average is : ", average)