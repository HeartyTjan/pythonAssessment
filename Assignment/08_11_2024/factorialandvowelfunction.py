def get_factorial(number):
	
	if not isinstance (number, int):
		
		raise ValueError ("Enter the correct input")

	if number < 0 :

		raise ValueError ("invalid input")

	factorial = 1

	for count in range(number, 0, -1):
		
		factorial = factorial * count

	return factorial

number = int(input("Enter a number : "))

factorial = get_factorial(number)

print(f"\nfactorial of {number} is : ", factorial)



def is_for_vowel(letter):

	if not isinstance (letter, str):

		print("invalid input")		

	vowel = ['a','e','i','o','u']

	size = len(vowel)
	counter = 0

	for word in list(vowel):

		
		if word == letter:
		
			counter = counter +1

	if counter == 1:
		return True

	else :
		return False	
			
			
letter = input("\nEnter a character : ")

print(is_for_vowel(letter))