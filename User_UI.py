from Account import *
from Bank import *
from AccountCreator import *
from LoanController import *
from Transfer import *


class User_UI:
    def __init__(self, bank: Bank) -> None:
        self.bank = bank
        self.account = None

    def user_menu(self):
        while True:
            print("\n\n")
            print("#############################################")
            print("|              Welcome User                 |")
            print("#############################################")
            if (self.account != None):
                print(self.account)

            print("0. Login\n1. Create an account")
            if (self.account != None):
                print("2. Deposit\n3. Withdrawal\n4. Check Balance\n5. Check Transaction History\n6. Take a loan\n7. Transfer Money\n8. Exit")
            choice = input("Enter your choice: ")

            if choice == '0':
                print("---------------------------------")
                print("Login")
                print("---------------------------------")
                account_number = int(input("Enter account_number: "))
                email = input("Enter email: ")
                account = self.bank.get_account(account_number, email)
                if account != None:
                    self.account = account
                    print("Login Successfull")
                else:
                    print("Account not found")

            elif choice == '1':
                print("---------------------------------")
                print("Create a user account")
                print("---------------------------------")

                account = AccountCreator().create_account()
                account = self.bank.create_account(account)
                self.account = account

            elif self.account and choice == '2':
                print("---------------------------------")
                print("Deposit")
                print("---------------------------------")
                amount = int(input("Enter deposit amount: "))

                self.account.deposit(amount)
                self.bank.increase_total_balance(amount)

            elif self.account and choice == '3':
                print("---------------------------------")
                print("Withdrawal")
                print("---------------------------------")

                money = int(input("Enter withdrawal amount: "))
                success = self.account.withdrawal(money)

                if success == False:
                    print("Withdrawal amount exceeded")

            elif self.account and choice == '4':
                print("---------------------------------")
                print("Check Balance")
                print("---------------------------------")

                print("Balance = ", self.account.get_balance())

            elif self.account and choice == '5':
                print("---------------------------------")
                print("Check Transaction history")
                print("---------------------------------")

                for t in self.account.get_transactions_history():
                    print(t)

            elif self.account and choice == '6':
                print("---------------------------------")
                print("Take Loan")
                print("---------------------------------")
                amount = int(input("Enter Loan Amount: "))

                if self.bank.get_loan_feature() == False:
                    print("Loan Feature is off")
                    return

                result = LoanController().createLoan(account=self.account,
                                                     bank=self.bank, loan_amount=amount)
                print(result)

            elif self.account and choice == '7':
                print("---------------------------------")
                print("Transfer Money")
                print("---------------------------------")
                to_account_number = int(input("Enter account number: "))
                amount = int(input("Enter amount to transfer: "))
                result = Transfer.make_transfer(
                    bank=self.bank, from_account=self.account, to_account_number=to_account_number, amount=amount)
                print(result)
                pass

            elif choice == '8':
                print("---------------------------------")
                print("Thank you for using our banking system!")
                print("---------------------------------")
                break

            else:
                print("---------------------------------")
                print("Invalid choice. Please try again.")
                print("---------------------------------")
