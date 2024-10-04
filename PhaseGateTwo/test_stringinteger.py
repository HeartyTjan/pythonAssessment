import unittest 
import stringinteger

class TestStringInteger(unittest.TestCase):
	
	def test_if_add_string_integer_exist(self):
		stringinteger.add_string_integer("1","2")

	def test_add_string_integer_return_expected_result(self):
		self.assertEqual(stringinteger.add_string_integer("1","2"),'3')
		self.assertEqual(stringinteger.add_string_integer("0","1"),'1')
		self.assertEqual(stringinteger.add_string_integer("0","0"),'0')
	
	def test_add_string_integer_return_expected_result_for_negative_value(self):
		self.assertEqual(stringinteger.add_string_integer("-1","-2"),'-3')
		self.assertEqual(stringinteger.add_string_integer("-2","-0"),'-2')
		self.assertEqual(stringinteger.add_string_integer("-0","-0"),'0')

	def test_add_string_integer_raises_error_for_floating_value(self):
		self.assertRaises(ValueError, stringinteger.add_string_integer,"1.3","4.6")
		self.assertRaises(ValueError, stringinteger.add_string_integer,-2.9,"-0")
		self.assertRaises(ValueError, stringinteger.add_string_integer, "7.76", -82.5)
		self.assertRaises(ValueError, stringinteger.add_string_integer, 10, 15)



