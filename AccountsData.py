from random import randint
class Account():
    """Account class to hold account attributes and Methods involving"""
    # Attributes
    accont_number=randint(11111111110,100000000000)
    balance=0
    accountholder=""
   
    # Methods
    def open_account(self,name,deposit):
        if len(self.accountholder)!=0:
           print("User already exists")
        else:
            self.accountholder=name
            self.deposit(self,deposit)

    def deposit(self,amount):
        """Takes in the deposit amount operate ( + )and return the new balance"""
        if self.accountholder:
            if amount>0:
                self.balance+=amount
                print(f"Amount deposited.\nAccount Balance : ${self.balance}")
            else:
                print("Deposit action failed 🧧\nTry again")
        else:
            print("No user account found")

    def withdrawl(self,amount):
        """Takes in the withdrawl amount operate ( - ) and return the new balance"""
        if self.accountholder:
            if amount<=self.balance:
                self.balance-=amount
                print("WithDrawl operation Success")
                print(f"\nAccount Balance : ${self.balance}")
            else:
                print("Your request exceeds you savings")
        else:
            print("No user account found")

    def get_balance(self):
        """Prints the current available balance"""
        if self.accountholder:
            print(f"Balance : ${self.balance}\n")
        else:
            print("Login your account to view details")



class Saving_Account(Account):
    """Saving Account Data Management class"""
    interest_rate=2.04
    def calculate_interest(self):
        if Account.accountholder:
            interest=self.interest_rate * (self.balance)
            print(f"Annual interest over your balance ${super().balance} is amount ${interest}\n")
        else:
            print("Login to your account for actions")



class CheckingAccount(Account):
    overdraft_limit=-50000

    def credit_withdraw(self,amount):
        if Account.accountholder:
            if self.balance>self.overdraft_limit:
                Account.balance -= amount
                self.overdraft_limit += amount
                print(f"\nAccount Balance : ${Account.balance}")
                print(f"\nCredits left --- Balance (C) :  ${self.overdraft_limit*-1}")
                print(" Message --- WithDrawl operation Success")
            else:
                print("Can't fulfil operation. You went out of limit.")
        else:
            print("Operation not valid.\nLogin to your account")