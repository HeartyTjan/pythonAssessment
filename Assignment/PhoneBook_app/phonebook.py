class PhoneBook:

	def __init__(self,first_name,last_name,phone_number):

		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.phone_number = phone_number

	
	def set_first_name(self, first_name):

		self.first_name = first_name


	def get_first_name(self):

		return self.first_name


	def set_last_name(self, last_name):

		self.last_name = last_name


	def get_last_name(self):

		return self.last_name


	def set_phone_number(self,phone_number):

		self.phone_number = phone_number

	def get_phone_number(self):

		return self.phone_number
	
	def display_info(self):

		print(f"\nFirst name : {self.first_name}")
		
		print(f"\nLast name : {self.last_name}")

		print(f"\nPhone number : {self.phone_number}\n")
		