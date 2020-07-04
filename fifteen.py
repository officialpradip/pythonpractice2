'''Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?'''

class BankCustomer:

    def __init__(self, balance):
        self._money = balance

    def deposit(self, bank):
        # depositcase

    def withdraw(self, bank):
        # withdraw case

    def balance(self):
        # remaining amount
        return self._money