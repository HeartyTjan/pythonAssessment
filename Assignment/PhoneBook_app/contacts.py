from phonebook import PhoneBook
import re

contacts = []


def save_prompt():
	
	print("\nprocessing >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

	print("successfull\n")	


def add_contact():

	print("""
		
		Add New Contact
	       ==================

	""")

	try:

		first_name = input("Enter first name : ")

		last_name = input("Enter last name : ")

		phone_number = input("Enter phone number : ")

		name_pattern = r'^[A-z][a-z]+$'

		phone_number_pattern = r'^[0][01789]{2}[0-9]{8}$'

		if re.search(name_pattern, first_name) and re.search(name_pattern, last_name):
	
			if re.search(phone_number_pattern, phone_number):

				contact = PhoneBook(first_name, last_name, phone_number)
		
				contacts.append(contact)

				save_prompt()

			else: 
				print("Enter a valid phone number")
		else:
			print("\nName must only consist of letter and start with capital letter")

	except ValueError:	
		print("Invalid Input")
				

def edit_first_name():
	
	print("""
		
		Edit first name 
	       ==================

	""")
	
	try :
	
		phone_number = input("Enter phone number to find Contact : ")

		user_contact = None

		for contact in contacts:
		
			if contact.get_phone_number() == phone_number:

				user_contact = contact	
				break

		if user_contact == None :

			return print("Enter a valid phone number")

		
		new_first_name = input("Enter new first name : ")
		
		name_pattern = r'^[A-z][a-z]+$'
		
		if re.search(name_pattern, new_first_name):
		
			user_contact.set_first_name(new_first_name)

			save_prompt()

		else:
			print("Enter a valid name")

	except ValueError:	
		print("Invalid Input")



def edit_last_name():
	
	print("""
		
		Edit Last name 
	       ==================

	""")
	
	try :
	
		phone_number = input("Enter phone number to find Contact : ")

		user_contact = None

		for contact in contacts:
		
			if contact.get_phone_number() == phone_number:

				user_contact = contact	
				break

		if user_contact == None :

			return print("Enter a valid phone number")

		
		new_last_name = input("Enter new last name : ")
		
		name_pattern = r'^[A-z][a-z]+$'
		
		if re.search(name_pattern, new_last_name):
		
			user_contact.set_last_name(new_last_name)

			save_prompt()

		else:
			print("Enter a valid name")

	except ValueError:	
		print("Invalid Input")


def edit_phone_number():
	
	print("""
		
	        Edit Phone Number
	       ==================

	""")
	
	try :
	
		phone_number = input("Enter phone number to find Contact : ")

		user_contact = None

		for contact in contacts:
		
			if contact.get_phone_number() == phone_number:

				user_contact = contact	
				break

		if user_contact == None :

			return print("Enter a valid phone number")

		
		new_phone_number = input("Enter new phone number : ")
		
		phone_number_pattern = r'^[0][01789]{2}[0-9]{8}$'
		
		if re.search(phone_number_pattern, new_phone_number):
		
			user_contact.set_phone_number(new_phone_number)

			save_prompt()

		else:
			print("Enter a valid phone number")


	except ValueError:	
		print("Invalid Input")


def find_contact_first_name():

	print("""
		
	        Find Contact Via First Name
	       =============================

	""")

	try :
		first_name = input("Enter first name to find Contact : ")

		if len(contacts) == 0:

			return print("No available contact")

		for contact in contacts:
		
			if contact.get_first_name() == first_name :

				contact.display_info()

			else:
				print("Enter valid name")
	
	except ValueError:	
		print("Invalid Input")

def find_contact_phone_number():

	print("""
		
	        Find Contact Via Phone Number
	       ================================

	""")

	try :
		phone_number = input("Enter phone number to find Contact : ")

		if len(contacts) == 0:

			return print("No available contact")

		for contact in contacts:
		
			if contact.get_phone_number() == phone_number:

				contact.display_info()

			else:
				print("Enter valid number")
	
	except ValueError:	
		print("Invalid Input")



def remove_contact():

	print("""
		
	        Remove Contact
	       ==================

	""")
	
	try :
	
		phone_number = input("Enter phone number to find Contact : ")

		user_contact = None

		for contact in contacts:
		
			if contact.get_phone_number() == phone_number :

				user_contact = contact	
				break

		if user_contact == None:

			return print("Enter a valid phone number")

		contacts.remove(user_contact)

		save_prompt()

	except ValueError:	
		print("Invalid Input")
		

				
			

		

	
