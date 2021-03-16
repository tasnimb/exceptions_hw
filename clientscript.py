from exception_handling import InsufficientFundsException
from account import Account
from savingsacc import Savings_Account

first_account=Account("Tasnim", "Begum", 900)

#setters
first_account.account_holder = "Sanele , Mbuthuma"

first_account.account_holder = "Manzeela, Ferdows"
print(first_account.account_holder)



#Instantiate our savings account
lisa_account=Savings_Account("Lisa", "Simpson", 300)


try:
    lisa_account.withdraw(1000)
except InsufficientFundsException as error:
    print(error)
else:
    print("Your remaining balance is :", lisa_account._balance)
finally:
    print("cleaning up...")

