import unittest

from class_work.account import Account

from decimal import Decimal



class TestAccount(unittest.TestCase):

    def setUp(self):
        self.babatunde = Account("babatunde", "09036011444")
    def test_that_account_exist(self):

        account1 = Account("babatunde", "09036011444")

        account2 = Account("Theezy", "09063475087")

    def test_that_you_can_deposit(self):


        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))

        self.babatunde.deposit(Decimal("100_000"))

        self.assertEqual(self.babatunde.get_balance(), Decimal("100_000"))



    def test_that_you_can_not_deposit_negative_amount(self):

        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))

        self.assertRaises(ValueError, self.babatunde.deposit,(Decimal("-100_000")))


    def test_that_you_can_withdraw(self):

        self.assertEqual(self.babatunde.get_balance(), Decimal("0.00"))
        self.babatunde.deposit(Decimal("100_000"))
        self.babatunde.withdraw(20_000)
        self.assertEqual(self.babatunde.get_balance(), Decimal("80_000"))

    def test_that_you_cant_withdraw_morethan_one_amount(self):
        babatunde = Account("babatunde", "09036041144")
        babatunde.deposit(80_000)
        self.assertEqual(babatunde.get_balance(), Decimal("80_000"))
        self.assertRaises(ValueError, babatunde.withdraw, 100_000)



