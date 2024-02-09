from User import *
from Bank import *


class User_Interface:
    def __init__(self, bank, account = None) -> None:
        self.bank = bank
        self.account = account

    def user_menu(self):
        print("Welcome User")

        while True:
            print("\n1. Create an account\n2. Deposit\n3. Withdrawal\n4. Check Balance\n5. Check Transaction History\n6. Take a loan\n7. Transfer Money\n8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                # Create an account
                print("Create new Account: ")
                name = input("Enter Your name: ")
                email = input("Enter Your email: ")
                address = input("Enter Your address: ")
                account_type = input(
                    "Enter Your account_type (Savings or Current): ")

                account = User(name=name, email=email, address=address,
                               account_type=account_type)
                self.bank.create_account(account)
                self.account = account

            elif choice == '2':
                # Deposit
                money = int(input("Enter deposit amount: "))
                self.account.deposit(money)

            elif choice == '3':
                # Withdrawal
                money = int(input("Enter withdrawal amount: "))
                success = self.account.withdrawal(money)
                
                if success == False:
                    print("Withdrawal amount exceeded")

            elif choice == '4':
                # Check Balance
                print("Balance = ", self.account.get_balance())

            elif choice == '5':
                # Check Transaction history
                for t in self.account.get_transactions_history():
                    print(t)

            elif choice == '6':
                # Take Loan
                pass

            elif choice == '7':
                # Transfer Money
                pass

            elif choice == '8':
                print("Thank you for using our banking system!")
                break

            else:
                print("Invalid choice. Please try again.")
