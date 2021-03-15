from account import Account
from exception_handling import InsufficientFundsException


class Savings_Account(Account):
    withdrawal_charge = 0.05

    def withdraw(self, withdraw_amount):
        if self._balance < withdraw_amount:
            raise InsufficientFundsException(f"There are insufficient funds available to withdraw from this account. \n"
                                             f"Your current balance is {self._balance}. You are trying to withdraw {withdraw_amount}. "
                                             f"You will be overdrawn by: {abs(self._balance - withdraw_amount)}")
        else:
            self._balance -= withdraw_amount + (withdraw_amount * self.withdrawal_charge)
            return
#extended the functionality of the withdraw method by adding a 5% withdraw charge
