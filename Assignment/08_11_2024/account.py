class Account:

	def __init__(self,first_name,last_name,account_number,pin):
		
		self.first_name = first_name
		self.last_name = last_name
		self.account_name = first_name + " " + last_name
		self.account_number = account_number
		self.pin = pin
		self.balance = 0;

	def get_account_name(self):
		
		return self.account_name

	def get_first_name(self):
		
		return self.first_name

	def get_last_name(self):

		return self.last_name

	def get_pin(self):

		return self.pin

	def deposit(self,amount):

		if(amount > 0.0):

			self.balance += amount

		else :
			return "Enter a valid amount"


	def withdraw(self,amount):

		if(amount <= balance):
			
			self.balance -= amount
		else :
			return "insufficient amount"


	def change_pin(self,new_pin):

		self.pin = new_pin

	def print_accounts(self):

		print(f" Account Name\t\t","\tAccount Number")

		print(f" {self.account_name:<15}\t{self.account_number:>20}")












