from Account import *


class AccountCreator:
    def create_account(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        account_type = input(
            "Enter account_type : Savings(1) or Current(2): ")

        account = Account(name=name, email=email, address=address,
                          account_type=account_type)
        return account
