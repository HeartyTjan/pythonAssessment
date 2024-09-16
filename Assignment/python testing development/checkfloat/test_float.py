import unittest
import float

class TestFloat(unittest.TestCase) :
	
	def test_float_function_exist(self):
		float.only_float(12.1,23)
	
	def test_float_function_return_result(self) :
		
		self.assertEqual(float.only_float(12.1,23), 1)
	
	def  test_float_function_raise_type_error_with_string_type(self) :
		self.assertRaises(TypeError, float.only_float, "Jesse")

