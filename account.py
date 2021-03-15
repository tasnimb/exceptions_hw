from exception_handling import InsufficientFundsException

class Account:
    numCreated = 0
    def __init__(self, f_name, l_name, initial_balance):

        self.f_name = f_name

        self.l_name = l_name

        self._balance = initial_balance

        Account.numCreated += 1


    @property
    def get_accountholder(self):
        return f"First name:{self.fname}\nSurname:{self.lname}"

    @get_accountholder.setter
    def get_accountholder(self,name):
        self.fname,self.lname= name.split(",")


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


