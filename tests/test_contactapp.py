import unittest
from Assignment import contactapp


class ContactsApp(unittest.TestCase):
    def test_add_contact_exist(self):
       contactapp.add_contact("Tijani","salami@gmail.com",9098128958)

    def test_add_contact_function_peform_expected_tasks(self):
        contactapp.add_contact("Tijani","salami@gmail.com",9098128958)




