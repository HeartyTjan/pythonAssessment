import unittest 
import divideorsquare

class TestDivideOrSquare(unittest.TestCase):
	
	def test_if_divide_or_square_function_exist(self):
		divideorsquare.divide_or_square(6)

	def test_if_divide_or_square_function_return_expected_value(self):
		self.assertEqual(divideorsquare.divide_or_square(10),3.16)
		self.assertEqual(divideorsquare.divide_or_square(25),5)
	
	def test_if_divide_or_square_function_raises_error_for_negative_value(self):
		self.assertRaises(ValueError, divideorsquare.divide_or_square, -10)
		self.assertRaises(ValueError, divideorsquare.divide_or_square, -25)

	def test_if_divide_or_square_function_raises_error_for_String_value(self):

		self.assertRaises(ValueError, divideorsquare.divide_or_square, "Abu")
		self.assertRaises(ValueError, divideorsquare.divide_or_square, "Fetch")

	def test_add_string_integer_raises_error_for_floating_value(self):
		self.assertRaises(ValueError, divideorsquare.divide_or_square, 10.6)
		self.assertRaises(ValueError, divideorsquare.divide_or_square, 25.0)


