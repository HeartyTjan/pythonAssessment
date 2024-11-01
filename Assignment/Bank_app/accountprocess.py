import random
import re
from account import Account

bank = []

def save_prompt():
	
	print("\nprocessing >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

	print("successfull\n")	

			
def open_account():
	
	try:
		print("""
			
		Open Account
		============
		""")

		first_name = input("What is your first name : ")

		last_name = input("What is your last name : ")

		pin = input("Enter your four digit pin : ")

		pin_pattern = r'^[0-9]{4}$'

		if re.search(pin_pattern,pin):

			name_pattern = r'^[A-Z]+[a-z]+$'

			if re.search(name_pattern, first_name) and re.search(name_pattern, last_name):
 
				account_number = "BB" + str(random.randint(1000000,100000000))
		
				account = Account(first_name,last_name,account_number,pin)
	
				bank.append(account)

				save_prompt()
			else:
				print("Name must only consist of letter and start with capital letter")

		else :
			print("Enter a four digit pin")

  
	except ValueError:	
		print("Invalid input")



def deposit():

	print("""
			
		Deposit Menu
		=============
	""")


	try:

		account_number = input("What is your account number: ")	
	
		amount = int(input("Enter amount to deposit: "))	

		for account in bank:
	
			if account.get_account_number() == account_number:
			
				account.deposit(amount)

				if(account.check_account_status() == True):
					save_prompt()

			else:
				print("Enter a valid account number")

	except ValueError:
		print("Invalid Input")

def withdraw():
	
	print("""
			
		Withdraw Menu
		==============
	""")

	try:

		account_number = input("Enter is your account number: ")
		pin = input("Enter your pin: ")	

		user_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_pin() == pin:

				user_account = account
				break

		if user_account == None:

			return print("Incorrect details ")


		print(f"\n    Welcome back {account.get_account_name()}")
		print("========================================\n")
			
		amount = int(input("Enter amount to withdraw: "))	

		account.withdraw(amount)

		save_prompt()

  
	except ValueError:
		print("Invalid input")


def dispay_balance():

	print("""
			
		  Check Balance
		=================
	""")

	try:

		account_number = input("Enter your account number: ")
		pin = input("Enter your pin: ")	
		user_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_pin() == pin:

				user_account = account
				break

		if user_account == None:
			return print("Incorrect details ")

		print(f"\n    Welcome back {account.get_account_name()}")
		print("========================================\n")
			
		print(f"Account balance is : {account.get_balance():,}")
					
	except ValueError:
		print("Invalid input")


def transfer():

	flag = False
	print("""
			
		Transfer Menu
		===============
		""")
	try:
	
		if len(bank) < 2:
			return print("There is only one account in the bank")

		
		account_number = input("Enter your account number: ")
		pin = input("Enter your pin: ")	

		sender_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_pin() == pin:

				sender_account = account
				break

		if sender_account is None:

			return print("Incorrect details")

			
		print(f"\n    Welcome back {sender_account.get_account_name()}")
		print("========================================\n")

		recipient_account_number = input("Enter recipient account number: ")

		amount = int(input("Enter is amount to transfer: "))

		recipient_account = None

		for account in bank:

			if account.get_account_number() == recipient_account_number:

				recipient_account = account
				break

		if recipient_account is None:
			return print("Incorrect recipient account details")

		sender_account.transfer(recipient_account,amount)
		flag = True

	except ValueError:

			print("Invalid input")
			
def change_user_pin():

	print("""
		
		Change Pin
	       =============
	""")


	try:
	
		account_number = input("Enter your account number: ")
		pin = input("Enter your pin: ")	

		user_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_pin() == pin:

				user_account = account
				break

		if user_account is None:

			return print("Incorrect details")

		new_pin = input("Enter new pin: ")	

		user_account.change_pin(new_pin)
		
		save_prompt()
	
 		
	except ValueError:
		print("Invalid input")


def check_user_pin():

	print("""
		
		Check Pin
	      =============
	""")

	try :
		account_number = input("Enter your account number: ")
		full_name = input("Enter your full name(Last name first): ")

		user_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_account_name() == full_name:
	
				user_account = account
				break

		if user_account is None:
			return print("Incorrect details")

		print(f"\n Your Pin is : {user_account.get_pin()}")

	except ValueError:
		print("Invalid input")

def close_account():

	print("""
		
		Change Account
	       =================
	""")

	try: 
	
		account_number = input("Enter your account number: ")
		pin = input("Enter your pin: ")	

		user_account = None

		for account in bank:
		
			if account.get_account_number() == account_number and account.get_pin() == pin:

				user_account = account
				break

		if user_account is None:

			return print("Incorrect details")


		user_account.close_account()
		
		save_prompt()

	except ValueError:
		print("Invalid Input")

		
def display_account_details():

	print("""
			
		Check Account Details
		======================
	""")


	try:

		full_name = input("What is your full name(Last name first): ")

		pin = input("Enter your pin: ")

		user_account = None
		
		for account in bank:

			if account.get_account_name() == full_name and account.get_pin() == pin:
			
				user_account = account
				break

		if user_account is None:
			return print("Incorrect details")

		user_account.print_accounts()
				
			
	except ValueError:
		print("Invalid input")

