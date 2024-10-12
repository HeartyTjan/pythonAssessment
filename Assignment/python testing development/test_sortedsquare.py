import unittest
import sortedsquare

class TestSortedSquare(unittest.TestCase):
	
	def test_if_get_square_function_exist(self):
		sortedsquare.get_square(10)

	def test_get_square_function_gives_expected_value(self):
		self.assertEqual(sortedsquare.get_square(5),25)
		self.assertEqual(sortedsquare.get_square(-3),9)
		self.assertEqual(sortedsquare.get_square(0),0)

	def test_get_square_function_gives_expected_value_for_floating_value(self):
		self.assertEqual(sortedsquare.get_square(5.2),27.04)
		self.assertEqual(sortedsquare.get_square(9.7),94.09)
		self.assertEqual(sortedsquare.get_square(0.0),0.0)

	def test_get_square_function_raises_error_exception_for_string_value(self):
		self.assertRaises(ValueError, sortedsquare.get_square,"Abu")

class TestSortedSquare(unittest.TestCase):

	def test_if_get_array_square_function_exist(self):
		sortedsquare.get_array_square([10,11,13])

	def test_if_get_array_square_function_return_correct_value(self):
		self.assertEqual(sortedsquare.get_array_square([4,3,5]),[16,9,25])
		self.assertEqual(sortedsquare.get_array_square([4,3,5,-7,-9]),[16,9,25,49,81])
		self.assertEqual(sortedsquare.get_array_square([0,3,5]),[0,9,25])
		self.assertEqual(sortedsquare.get_array_square([4,3,5]),[16,9,25])

	def test_if_get_array_square_function_raises_error_if_contain_string_element(self):
		self.assertRaises(ValueError, sortedsquare.get_array_square, [1,3,"Two",8,4])

	def test_get_array_square_function_gives_expected_value_for_floating_value(self):
		self.assertEqual(sortedsquare.get_array_square([5.2,2.6,6]),[27.04,6.76,36])
		self.assertEqual(sortedsquare.get_array_square([-9.7,5,9]),[94.09,25,81])
		self.assertEqual(sortedsquare.get_array_square([0.0,2,-1.1]),[0.0,4,1.1])


class TestSortedSquare(unittest.TestCase):

	def test_if_sort_array_function_exist(self):
		sortedsquare.sort_array([13,11,9,7,15])

	def test_if_sort_array_function_return_correct_value(self):
		self.assertEqual(sortedsquare.sort_array([4,3,5]),[3,4,5])
		self.assertEqual(sortedsquare.sort_array([4,3,5,0]),[0,3,4,5])
		self.assertEqual(sortedsquare.sort_array([14,32,75,13]),[13,14,32,75])

	def test_if_sort_array_function_return_correct_value_for_negative_value(self):
		self.assertEqual(sortedsquare.sort_array([14,-32,75,-13]),[-32,-13,14,75])
		self.assertEqual(sortedsquare.sort_array([-4,-3,-5]),[-5,-4,-3])
		self.assertEqual(sortedsquare.sort_array([-14,-32,-75,-13]),[-75,-32,-14,-13])

	def test_get_array_square_function_gives_expected_value_for_floating_value(self):
		self.assertEqual(sortedsquare.sort_array([5.2,2.6,6]),[2.6,5.2,6])
		self.assertEqual(sortedsquare.sort_array([-9.7,5,9]),[-9.7,5,9])
		self.assertEqual(sortedsquare.sort_array([0.0,2,-1.1]),[-1.1,0.0,2])

	def test_if_sort_array_function_raises_error_if_contain_string_element(self):
		self.assertRaises(ValueError, sortedsquare.sort_array, [1,3,"Two",8,4])




