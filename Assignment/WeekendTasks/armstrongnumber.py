'''
def is_armstrong(digit):

	number = str(digit)[:: -1]

	size = len(number)

	total = 0

	for count in range(size):
	
		num = int(number[count])
	
		total += pow(num,size)
	
	if total == digit:

		return True
	
	else :
		return False


digit = int(input("Enter a number : "))

	
for number in range(digit):

	states = is_armstrong(number)

	if states:
		print(number) 
'''

letter = "g"
vowel = "aeiou"

for word in vowel:

	if word == letter:
		print("True")
		break
	else:
		continue
if letter != vowel[len(vowel)-1]:
	print("False")