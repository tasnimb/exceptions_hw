from account import Account


class Saving_Account(Account):



    # def __init__(self, initial_balance):
    #     super().__init__()

    def deposit(self, amount):
        self._balance += amount
        return
    def get_balance(self):
        return self._balance

    # def add_interest(self):






