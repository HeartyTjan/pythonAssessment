import swaparray
import unittest

class TestSwappArray(unittest.TestCase):

	def test_if_swap_function_exist(self):
		swaparray.swap([1,2,3,4,5,6])

	def test_swap_function_return_correct_value(self):
		self.assertEqual(swaparray.swap([1,2,3,4,5,6]),[2,1,4,3,6,5])	

	def test_swap_function_return_correct_value_for_negative_value(self):
		self.assertEqual(swaparray.swap([1,2,3,-4,-5,6]),[2,1,-4,3,6,-5])

	def test_swap_function_correct_value_for_String_element_in_list(self):
		self.assertEqual(swaparray.swap(["hey",2,3,4,"a",6]),[2,"hey",4,3,6,"a"])	

	def test_swap_function_raises_error_for_int_value(self):
		self.assertRaises(ValueError, swaparray.swap, 50)

	def test_swap_function_raises_error_for_String_value(self):
		self.assertRaises(ValueError, swaparray.swap, "Ademide")