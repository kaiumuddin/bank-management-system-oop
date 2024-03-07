from Bank import *
from Account import *
from AccountCreator import *


class Admin_UI:
    def __init__(self, bank) -> None:
        self.bank = bank

    def admin_menu(self):
        while True:
            print("\n\n")
            print("#############################################")
            print("|              Welcome Admin                |")
            print("#############################################")

            print("1. Create an account\n2. Delete Account\n3. View All Accounts\n4. Check Total Balance\n5. Check Total Loan Amount\n6. Toggle Loan Feature\n7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("---------------------------------")
                print("Create a user account")
                print("---------------------------------")

                account = AccountCreator().create_account()
                self.bank.create_account(account)

            elif choice == '2':
                print("---------------------------------")
                print("Delete account")
                print("---------------------------------")

                account_number = int(input("Enter account number: "))
                self.bank.delete_account(
                    account=self.bank.get_account(account_number))

            elif choice == '3':
                print("---------------------------------")
                print("View all accounts")
                print("---------------------------------")

                print("All Accounts: ")
                for account in self.bank.get_all_accounts():
                    print(account)

            elif choice == '4':
                print("---------------------------------")
                print("Check total balance")
                print("---------------------------------")

                print("Total Balance: ", self.bank.get_total_balance())

            elif choice == '5':
                print("---------------------------------")
                print("Check total loan amount")
                print("---------------------------------")

                print("Total Loan: ", self.bank.get_loan_amount())

            elif choice == '6':
                print("---------------------------------")
                print("Toggle loan feature")
                print("---------------------------------")

                value = self.bank.get_loan_feature()
                self.bank.set_loan_feature(value=not value)
                print("Loan feature change to : ",
                      self.bank.get_loan_feature())

            elif choice == '7':
                print("---------------------------------")
                print("Exiting Admin Panel.")
                print("---------------------------------")
                break

            else:
                print("---------------------------------")
                print("Invalid choice. Please try again.")
                print("---------------------------------")
