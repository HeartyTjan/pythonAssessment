import unittest
import arrayarrangement

class TestDescendingOrder(unittest.TestCase):

	def test_if_descending_order_function_exist(self):
		arrayarrangement.descending_order([5,2,7,1,8,2])

	def test_if_descending_order_function_return_expected_value(self):
		self.assertEqual(arrayarrangement.descending_order([5,2,7,1,8,2]),[8,7,5,2,2,1])
		self.assertEqual(arrayarrangement.descending_order([5,0,10,1,8,2]),[10,8,5,2,1,0])

	def test_if_descending_order_function_return_expected_value_negative_value(self):
		self.assertEqual(arrayarrangement.descending_order([-5,2,7,1,-8,2]),[7,2,2,1,-5,-8])
		self.assertEqual(arrayarrangement.descending_order([5,-2,-7,1,8,2]),[8,5,2,1,-2,-7])

	def test_if_descending_order_function_raises_error_for_String_value(self):
		self.assertRaises(ValueError,arrayarrangement.descending_order,([-5,2,7,"ade",-8,2]))
		#self.assertEqual(arrayarrangement.descending_order([5,-2,-7,1,8,2]),[8,5,2,1,-2,-7])



	def test_if_ascending_order_function_exist(self):
		arrayarrangement.ascending_order([5,2,7,1,8,2])

	def test_if_ascending_order_function_return_expected_value(self):
		self.assertEqual(arrayarrangement.ascending_order([5,2,7,1,8,2]),[1,2,2,5,7,8])
		self.assertEqual(arrayarrangement.ascending_order([5,0,10,1,8,2]),[0,1,2,5,8,10])

	def test_if_ascending_order_function_return_expected_value_negative_value(self):
		self.assertEqual(arrayarrangement.ascending_order([-5,2,7,1,-8,2]),[-8,-5,1,2,2,7])
		self.assertEqual(arrayarrangement.ascending_order([5,-2,-7,1,8,2]),[-7,-2,1,2,5,8])

	def test_if_ascending_order_function_raises_error_for_String_value(self):
		self.assertRaises(ValueError,arrayarrangement.ascending_order,([-5,2,7,"ade",-8,2]))
		

	def test_if_multiply_third_index_function_exist(self):
		arrayarrangement.multiply_third_index([5,2,7,1,8,2])

	def test_if_multiply_third_index_function_return_correct_value(self):
		self.assertEqual(arrayarrangement.multiply_third_index([5,2,7,1,8,2]),14)

	def test_if_multiply_third_index_function_return_correct_value(self):
		self.assertEqual(arrayarrangement.multiply_third_index([5,2,7,1,8,2]),14)




		




		