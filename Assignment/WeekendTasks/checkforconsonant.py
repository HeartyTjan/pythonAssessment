import string

def checkconsonant(sentence):

	TEXT = string.ascii_lowercase
	sentence = sentence.lower()
	count = 0
	letters = [word for word in TEXT]
	
	for letter in letters:
	
		if sentence.__contains__(letter):

			count += 1

			if count >= 26:
				
				return True
		else:
			return False
	


sentence = "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent."
phrase = "Waltzbadnymphforquickjigsvex"
print(checkconsonant(sentence))
print(checkconsonant(phrase))