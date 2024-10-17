

def binary_search(array,find_value):

	start = 0
	end = len(array) -1
	
	
	while start <= end:
		
		mid = (start + end) // 2

		guess = array[mid]

		if guess == find_value:

			return mid

		if guess > find_value:

			end = mid - 1

		else:
			start = mid + 1

	return None


numbers = [1,2,4,5,6,7,17,45,67,89,94,97,130]
find_number = 97

output = binary_search(numbers,find_number)

if output != None:
	print(f"The index is : {output} and the value is : {numbers[output]}")
else:
	print("Element not find")