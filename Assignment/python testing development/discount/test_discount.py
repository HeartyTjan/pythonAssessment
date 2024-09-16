import unittest
import discount

class TestDiscount(unittest.TestCase):

	def  test_discount_function_exist(self) :
		discount.my_discount(150,15)


	def test_discount_functionreturn_floating_value_and_result(self) :
		
		self.assertEqual(discount.my_discount(150,15)
, 127.5)
	
	
	def test_discount_function_raise_type_error_with_non_integer_for_discount(self) :
		self.assertRaises(TypeError, discount.my_discount, 105,15.7)

	def test_discount_function_raise_type_error_with_string_type(self) :
		self.assertRaises(TypeError, discount.my_discount, "150")

	def test_discount_function__raise_error_with_negative_amount(self) :
		self.assertRaises(ValueError, discount.my_discount, -150,-15)

