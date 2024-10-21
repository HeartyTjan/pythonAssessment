import unittest
import passwordgenerator
import string
class TestPasswordGenerator(unittest.TestCase):

	def test_if_get_password_function_exist(self):
		passwordgenerator.get_password()


	def test_get_password_function_return_expected_length(self):
		password = passwordgenerator.get_password()
		self.assertTrue(len(password)> 15)

	def test_get_password_function_contains_lowercase_letter(self):
		
		password = passwordgenerator.get_password()
		self.assertTrue(any(value for value in password if value.islower()))

	def test_get_password_function_contains_uppercase_letter(self):
		
		password = passwordgenerator.get_password()
		self.assertTrue(any(value for value in password if value.isupper()))

	def test_get_password_function_contains_symbol(self):
		
		SYMBOLS = string.punctuation
		password = passwordgenerator.get_password()
		self.assertTrue(any(value for value in password if SYMBOLS.__contains__(value)))

	def test_get_password_function_contains_digit(self):
		
		password = passwordgenerator.get_password()
		self.assertTrue(any(value for value in password if value.isdigit()))



	