from exception_handling import InsufficientFundsException
from account import Account
from savingsacc import Saving_Account

first_account=Account("Tasnim", "Begum", 900)

#setters
first_account.get_accountholder= "balh,Mbuthuma"

first_account.get_accountholder="Manzeela, Ferdows"
print(first_account.get_accountholder)




lisa_account=Saving_Account("Lisa","Simpson",300)
print(lisa_account.get_balance())

try:
    lisa_account.withdraw(1000)
except InsufficientFundsException as error:
    print(error)
else:
    print("Your remaining balance is :", lisa_account._balance)
finally:
    print("cleaning up...")

