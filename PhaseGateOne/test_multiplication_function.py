import unittest
import multiplicationfunction

class TestMultiplication(unittest.TestCase):

	def test_get_product_function_exist(self) :
		multiplicationfunction.get_product(4,5)

	def test_get_product_function_return_correct_value(self):
		self.assertEqual(multiplicationfunction.get_product(4,4),16)
		self.assertEqual(multiplicationfunction.get_product(2,4),8)
		self.assertEqual(multiplicationfunction.get_product(4,2),8)
		self.assertEqual(multiplicationfunction.get_product(110,98),10_780)


	def test_get_product_function_return_correct_value_for_negative_number(self):
		self.assertEqual(multiplicationfunction.get_product(-2,4),-8)
		self.assertEqual(multiplicationfunction.get_product(4,-2),-8)
		self.assertEqual(multiplicationfunction.get_product(-48,-4),192)

	def test_get_product_function_raises_error_for_string_type(self):
		self.assertRaises(ValueError, multiplicationfunction.get_product,"ab","dele")
		self.assertRaises(ValueError, multiplicationfunction.get_product, 4 ,"dele")
		self.assertRaises(ValueError, multiplicationfunction.get_product,"ab", 7 )

	def test_get_product_function_return_correct_value_for_floating_number(self):
		self.assertEqual(multiplicationfunction.get_product(2,4.0),8.0)
		self.assertEqual(multiplicationfunction.get_product(2.0,4),8.0)
		self.assertEqual(multiplicationfunction.get_product(2.2,4.2),9.24)
		
	
	
