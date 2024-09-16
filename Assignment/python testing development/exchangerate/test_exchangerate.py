import unittest
import exchangerate

class TestExchangeRate(unittest.TestCase):

	def  test_exchange_rate_function_exist(self) :
		exchangerate.get_exchange_rate(100)


	def test_exchange_rate_function_return_floating_value_and_result(self) :
		
		self.assertEqual(exchangerate.get_exchange_rate(100.00), 155000.00)
		self.assertEqual(exchangerate.get_exchange_rate(10.00), 15500.00)
	
	def test_exchange_rate_function__raise_error_with_negative_amount(self) :
		self.assertRaises(ValueError, exchangerate.get_exchange_rate, -100.00)

	def test_cube_function_raise_type_error_with_string_type(self) :
		self.assertRaises(TypeError, exchangerate.get_exchange_rate, "Jesse")

