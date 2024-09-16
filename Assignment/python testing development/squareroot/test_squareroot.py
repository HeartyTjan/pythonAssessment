import unittest
import squareroot

class TestExchangeRate(unittest.TestCase):

	def  test_squareroot_function_exist(self) :
		squareroot.get_squareroot(10)

	def test_squareroot_function__raise_error_with_negative_amount(self) :
		self.assertRaises(ValueError,squareroot.get_squareroot, -100)

	def test_squareroot_function__raise_error_with_non_integer_value(self) :
		self.assertRaises(TypeError,squareroot.get_squareroot, 10.0)

	def test_squareroot_function_return_floating_value_and_result(self) :
		
		self.assertEqual(squareroot.get_squareroot(10), 3.16)
		

	def  test_squareroot_function_raise_type_error_with_string_type(self) :
		self.assertRaises(TypeError, squareroot.get_squareroot, "Jesse")

