
	
import random
import string

def get_password():

	TEXT_LOWERCASE = string.ascii_lowercase
	TEXT_UPPERCASE = string.ascii_uppercase
	SYMBOLS = string.punctuation

	pseudo_password = ""
	password = ""

	for _ in range(9):

		pseudo_password += random.choice(TEXT_LOWERCASE)
		pseudo_password += random.choice(TEXT_UPPERCASE)
		pseudo_password +=  str(random.randrange(1,10))
		pseudo_password += random.choice(SYMBOLS)

	size = random.randrange(15,30)
	
	for count in range(size):
		
		password += random.choice(pseudo_password)
			

	return password

