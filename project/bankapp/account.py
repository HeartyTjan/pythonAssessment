from decimal import Decimal
import random


class Account:
    def __init__(self, name: str, phone_number: str, pin) -> None:
        self.name = name
        self.phone_number = self.set_phone_number(phone_number)
        self.balance = Decimal('0.00')
        self.pin = pin
        self.account_number = self.generate_account_number()

    def set_phone_number(self, phone_number: str):
        if len(phone_number) != 11:
            raise ValueError('Number must be 11 characters long')
        self.phone_number = phone_number
        return self.phone_number

    def change_pin(self, default_pin: str, new_pin: str):
        if self.pin == default_pin:
            self.pin = new_pin

    def generate_account_number(self):
        self.account_number = "22" + str(random.randint(1000000, 100000000))
        return self.account_number


    def get_balance(self) -> Decimal:
        return self.balance

    def validate_balance(self, amount: Decimal):
        if amount < Decimal("0.00"):
            return "Invalid Balance"
        self.balance = amount
        return self.balance

    def deposit(self, amount: Decimal):
        self.validate_amount(amount)
        self.balance += amount

    def validate_amount(self, amount):
        if amount < Decimal("0.00"):
            raise ValueError

    def withdraw(self, amount):
        self.validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
