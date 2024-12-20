from unittest import TestCase

from class_work.person import Person


class TestPerson (TestCase):
    def test_constructor_exist(self):
        person = Person("Bola", 21)

    def test_constructor_initialize_and_return_expected_value(self):
        person = Person("Bola", 21)
        expected_value = "Bola", 21
        result = person.get_full_name(), person.get_age()
        self.assertEqual(expected_value, result)

    def test_constructor_throws_value_error_if_name_is_empty(self):
        person = Person("", 21)
        expected_error = "Name cannot be empty"
        self.assertEqual(expected_error, person.get_full_name())


    def test_get_full_name_return_expected_value(self):
        person = Person("Bola", 21)
        result = person.get_full_name()
        self.assertEqual(result, "Bola")

    def test_get_age_return_expected_value(self):
        person = Person("Bola", 21)
        result = person.get_age()
        self.assertEqual(result, 21)

    def test_get_age_throws_value_error_if_age_is_outside_200_range(self):
        person = Person("Bola", 211)
        expected_error = "Age must not be outside 200 range"
        self.assertEqual(expected_error, person.get_age())

    def test_greet_return_expected_value(self):
        person = Person("Bola", 21)
        result = person.greet()
        print()
        self.assertEqual(result, ("Hello", Bola))
