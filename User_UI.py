from Account import *
from Bank import *
from AccountCreator import *


class User_UI:
    def __init__(self, bank) -> None:
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

            print("0. Login\n1. Create an account\n2. Deposit\n3. Withdrawal\n4. Check Balance\n5. Check Transaction History\n6. Take a loan\n7. Transfer Money\n8. Exit")
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

            elif choice == '2':
                print("---------------------------------")
                print("Deposit")
                print("---------------------------------")
                amount = int(input("Enter deposit amount: "))

                self.account.deposit(amount)
                self.bank.increase_total_balance(amount)

            elif choice == '3':
                print("---------------------------------")
                print("Withdrawal")
                print("---------------------------------")

                money = int(input("Enter withdrawal amount: "))
                success = self.account.withdrawal(money)

                if success == False:
                    print("Withdrawal amount exceeded")

            elif choice == '4':
                print("---------------------------------")
                print("Check Balance")
                print("---------------------------------")

                print("Balance = ", self.account.get_balance())

            elif choice == '5':
                print("---------------------------------")
                print("Check Transaction history")
                print("---------------------------------")

                for t in self.account.get_transactions_history():
                    print(t)

            elif choice == '6':
                print("---------------------------------")
                print("Take Loan")
                print("---------------------------------")
                pass

            elif choice == '7':
                print("---------------------------------")
                print("Transfer Money")
                print("---------------------------------")
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

