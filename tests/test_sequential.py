import unittest
from class_work import sequential


class MyTestCase(unittest.TestCase):
    def test_get_sequential_list_function_exist(self):
        sequential.get_sequential_list()  #

    def test_get_sequential_list_function_return_expected_result(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  #
        self.assertEqual(sequential.get_sequential_list(), numbers)

    def test_duplicate_function_exist(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        sequential.duplicate(numbers)

    def test_duplicate_function_return_expected_values(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15,
                    15]
        self.assertEqual(sequential.duplicate(numbers), expected)

    def test_remove_duplicate_function_exist(self):
        sequential.remove_duplicate([1, 1, 2, 2])

    def test_remove_duplicate_function_return_expected_values(self):
        numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15,
                   15]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(sequential.remove_duplicate(numbers), expected)

    def test_sum_third_element_function_exist(self):
        sequential.sum_third_element([1, 2, 3, 4, 5])

    def test_sum_third_element_function_return_expected_values(self):
        actual = sequential.sum_third_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        expected = 45
        self.assertEqual(expected, actual)

    def test_sum_third_element_function_throw_exception_for_string_value(self):
        self.assertRaises(TypeError,sequential.sum_third_element,([1, 2, 'a', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))


if __name__ == '__main__':
    unittest.main()
