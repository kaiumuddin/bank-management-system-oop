from Admin import *
from Bank import *


class Admin_Interface:
    def __init__(self,bank, admin = None) -> None:
        self.bank = bank
        self.admin = admin

    def admin_menu(self):
        print("Welcome Admin : ", self.admin.name)

        while True:
            print("\n1. Create an account\n2. Delete Account\n3. View All Accounts\n4. Check Total Balance\n5. Check Total Loan Amount\n6. Toggle Loan Feature\n7. Exit")
            choice = input("Enter your choice: ")
            print(choice)

            if choice == '1':
                # Create an account
                print("Create new Account: ")
                name = input("Enter Your name: ")
                email = input("Enter Your email: ")
                password = input("Enter Your address: ")

                account = Admin(name=name, email=email, password=password)
                self.bank.create_admin(account)


            elif choice == '2':
                # delete_account
                account_number = int(input("Enter account number: "))
                self.bank.delete_account(
                    admin=self.admin, account=self.bank.get_account(account_number))


            elif choice == '3':
                # view_all_accounts
                for account in self.bank.get_all_accounts(admin=self.admin):
                    print(account)

            elif choice == '4':
                # check_total_balance
                print(self.bank.get_total_balance(admin=self.admin))

                
            elif choice == '5':
                # check_total_loan_amount
                print(self.bank.get_loan_amount(admin=self.admin))


            elif choice == '6':
                # toggle_loan_feature
                value = self.bank.get_loan_feature(admin=self.admin)
                self.bank.set_loan_feature(admin=self.admin, value=not value)


            elif choice == '7':
                print("Exiting Admin Panel.")
                break


            else:
                print("Invalid choice. Please try again.")
