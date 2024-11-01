import random
bank = []

class Account:

	def __init__(self,first_name,last_name,account_number,pin):
		
		self.first_name = first_name
		self.last_name = last_name
		self.account_name = last_name + " " + first_name
		self.account_number = account_number
		self.pin = pin
		self.balance = 0.0
		self.account_status = True

	def get_account_name(self):
		
		return self.account_name


	def get_first_name(self):
		
		return self.first_name


	def get_last_name(self):

		return self.last_name


	def get_balance(self):	
	
		return self.balance


	def get_account_number(self):

		return self.account_number

	def check_account_status(self):

		return self.account_status


	def get_pin(self):

		return self.pin


	def deposit(self,amount):

		if self.account_status is False:
			
			return print("Account is closed")

		if amount > 0.0:

			self.balance += amount

		else :
			print("Enter a valid amount")



	def withdraw(self,amount):

		if self.account_status:

			if amount <= self.balance:
			
				self.balance -= amount

			else:
				print("insufficient amount")

		else :
			print("Account closed")


	def transfer(self,recipient_account,amount):
	

		if self.account_status:

			if self.balance < amount:
				print("Transfer failed")

			else :
				self.balance -= amount
				recipient_account.balance += amount
				print(f"Successfully transferred {amount:,} to {recipient_account.get_account_name()}")
		else:
			print("Account is closed")
		

	def change_pin(self,new_pin):

		if self.accountstatus:

			self.pin = new_pin

		else :
			print("Account is closed")


	def print_accounts(self):

		if self.account_status:

			status = "Open"
		else:
			status = "Closed"

		print(f"\n Account Name\t\t","\tAccount Number\tStatus")

		print(f" {self.account_name:<15}\t{self.account_number:>20}\t{status:>5}")



	def close_account(self):

		if self.account_status and self.balance == 0.0:
		
			self.account_status = False







