from exception_handling import InsufficientFundsException

class Account:
    numCreated = 0
    def __init__(self, first_name, last_name, initial_balance):

        self._first_name = first_name

        self._last_name = last_name

        self._balance = initial_balance

        Account.numCreated += 1


    @property
    def account_holder(self):
        return f"First name:{self._first_name}\nSurname:{self._last_name}"

    @account_holder.setter
    def account_holder(self, name):
        self._first_name, self._last_name= name.split(",")


    def withdraw(self, withdraw_amount):

        if self._balance<withdraw_amount:
            raise InsufficientFundsException(f"There are insufficient funds available to withdraw from this account. \n"
                                             f"Your current balance is {self._balance}. You are trying to withdraw {withdraw_amount}. "
                                             f"You will be overdrawn by: {abs(self._balance - withdraw_amount)}")

        else:
            self._balance -= withdraw_amount
            return

    def deposit(self, amount):
        self._balance += amount
        return


