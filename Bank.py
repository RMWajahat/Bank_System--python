from AccountsData import Account,CheckingAccount,Saving_Account
from bank_art import bank_logo,open_account
from os import system
from prettytable import PrettyTable

def menu():
    """Prints the menu of options"""
    print("""\nChoice Menu
          1. Create Account
          2. Deposit
          3. Withdraw
          4. Withdraw on credit card
          5. Report
          """)
    
# Creating instances
Accounts=Account()
CheckinAccount=CheckingAccount()
SavingAccount=Saving_Account()
table=PrettyTable()

EXIT=False
while not EXIT:
    if input("Want to make bank tour? (Yes or No)").lower().strip()=="yes":
        print(bank_logo)
        menu()
        choice = input("NOTE: Type Create Account e.t.c\n\nChoice : ").lower().strip()
        system("cls")
        match choice:
            case "create account":
                print(open_account)
                Account.open_account(Account,name=input("Type in your name : "),deposit=round(float(input("Enter your deposit amount : ")),2))
                print(f"Account creation operation successful.\nYour new balance is --- Balance: ${Account.balance}")
            case "deposit":
                deposit = round(float(input("Enter your deposit amount : ")),2)
                Account.deposit(Account,amount=deposit)
            case "withdraw":
                withdraw = round(float(input("Enter your withdrawl amount : ")),2)
                Account.withdrawl(Account,amount=withdraw)
            case "withdraw on credit card":
                if input("Are yo sure you want to awail credit services? (Yes or No)").lower().strip()=="yes":
                    withdraw = round(float(input("Enter your withdrawl amount : ")),2)
                    CheckinAccount.credit_withdraw(amount=withdraw)
            case "report":
                table.add_column("REPORT",["Account Holder","Account Number","Balance"])
                table.align='l'
                table.add_column("",[f"{Account.accountholder}",f"{Account.accont_number}",f"${Account.balance}"])
                print(table)
            case _:
                print("Invalid choice made")
        system("pause")
        system("cls")
    else:
        EXIT=True