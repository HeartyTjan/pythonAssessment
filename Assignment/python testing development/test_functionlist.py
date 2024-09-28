import unittest
import functionlist

class TestLargest(unittest.TestCase):
	
	def test_if_get_largest__function_exist(self) :
		functionlist.get_largest([10,20,21,24])

	def test_if_get_largest_return_correct_result(self):
		self.assertEqual(functionlist.get_largest([10,20,40,50.8]), 50.8)

	def test_raise_eror_if_get_largest_is_not_list(self):
		self.assertRaises(TypeError,functionlist.get_largest, "bolu")

class TestReverse(unittest.TestCase):

	def test_if_get_reverse__function_exist(self) :
		functionlist.get_reverse([10,20,21,24])

	
	def test_if_get_reverse_return_correct_result(self):
		result = functionlist.get_reverse([10,20,40,50.8])
		self.assertEqual(result , [50.8,40,20,10])

class TestCheckElement(unittest.TestCase):

	def test_if_check_element_function_exist(self) :
		functionlist.check_element([10,20,21,24],10)

	
	def test_if_check_element_return_correct_result(self):			
		self.assertIn(functionlist.check_element([59,20,30,40],9), [True,False])
		self.assertIn(functionlist.check_element([59,-20,30,40],9), [True,False])
		self.assertIn(functionlist.check_element([59,-20,30,40],-20), [True,False])
		self.assertIn(functionlist.check_element(['bo','ho','fo','do'],'fo'), [True,False])
		self.assertIn(functionlist.check_element(['bo','ho',20,'do'],20), [True,False])


	def test_print_even_position_raise_Error_if_not_type_list(self):		
		self.assertRaises(TypeError,functionlist.print_even_positions, -30)


class TestPrintOddPositions(unittest.TestCase):
	
	def test_print_odd_positions_function_exist(self) :
		functionlist.print_odd_positions([10,20,21,24])


	def test_print_odd_position_return_correct_result(self):			
		self.assertEqual(functionlist.print_odd_positions([59,20,30,40]),[20,40])
		self.assertEqual(functionlist.print_odd_positions([59.9,-20,30,-40]),[-20,-40])
		self.assertEqual(functionlist.print_odd_positions([59.9,-20,30,-40,'ab','for']),[-20,-40,'for'])


	def test_print_odd_position_raise_Error_if_not_type_list(self):		
		self.assertRaises(TypeError,functionlist.print_odd_positions, 30)


class TestPrintEvenPositions(unittest.TestCase):
	
	def test_print_even_positions_function_exist(self) :
		functionlist.print_even_positions([10,20,21,24,79])


	def test_print_even_position_return_correct_result(self):			
		self.assertEqual(functionlist.print_even_positions([59,20,30,40,80]),[59,30,80])
		self.assertEqual(functionlist.print_even_positions([59.9,-20,30.80,-40]),[59.9,30.80])
		self.assertEqual(functionlist.print_even_positions([59.9,-20,30,-40,'ab','for']),[59.9, 30,'ab'])
	

	def test_print_even_position_raise_Error_if_not_type_list(self):		
		self.assertRaises(TypeError,functionlist.print_even_positions, -30)

class TestStringPalindrome(unittest.TestCase):

	
	def test_string_is_palindrome_function_exist(self) :
		functionlist.string_is_palindrome(["r","a","d","a","r"])


	def test_string_is_palindrome_function_raises_error_if_not_type_list(self):
		self.assertRaises(TypeError,functionlist.string_is_palindrome, 'abu')

		
	def test_string_is_palindrome_return_correct_result(self):			
		self.assertEqual(functionlist.string_is_palindrome(["r","a","d","a","r"]),True)  

class TestConcatinateList(unittest.TestCase):
	
	def test_concatinate_list_function_exist(self) :
		functionlist.concatinate_list([10,20,21,24,79], [81,86,90,93,97,100])


	def test_concatinate_list_function_return_correct_result(self):
		self.assertEqual(functionlist.concatinate_list([10,20,21,24,79], [81,86,90,93,97,100]), [10,20,21,24,79,81,86,90,93,97,100])

		self.assertEqual(functionlist.concatinate_list([10,20,21,-24,79], [81,86,90,93,-97,100]), [10,20,21,-24,79,81,86,90,93,-97,100])

		self.assertEqual(functionlist.concatinate_list([10,'abu',21,-24,79], [81,86,90,93,-97,'deer']), [10,'abu',21,-24,79,81,86,90,93,-97,'deer'])


	def test_concatinate_list_function_raises_error_if_not_type_list(self):
		
		#self.assertRaises(TypeError,functionlist.concatinate_list(10, [81]))
	
		#self.assertRaises(TypeError,functionlist.concatinate_list("deer", [81,86,90,93,97,100]))

		self.assertRaises(TypeError,functionlist.concatinate_list(-[10], [81,86,90,93,97,100]))
