from exception_handling import InsufficientFundsException
class Account:
    numCreated = 0
    def __init__(self, fname , lname, initial_balance):
        self.fname = fname
        self.lname = lname
        self._balance = initial_balance


        Account.numCreated += 1
    @property
    def get_accountholder(self):
        return f"First name:{self.fname}\nSurname:{self.lname}"

    @get_accountholder.setter
    def get_accountholder(self,name):
        self.fname,self.lname= name.split(",")

    # @property
    # def get_age(self):
    #
    #    return self.get_age
    #
    # @get_age.setter
    # def get_age(self, age):
    #    self.get_age=age




    def withdraw(self, withdraw_amount):
        if self._balance<withdraw_amount:
            raise InsufficientFundsException("There are insufficient funds available to withdraw from this account. " ,
            "Your current balance is {}. You are trying to withdraw {}.".format(self._balance, withdraw_amount),
            " You will be overdrawn by: ", abs(self._balance - withdraw_amount))

        else:
            self._balance -= withdraw_amount
            return

    def deposit(self,amount):
        self._balance+=amount
        return


