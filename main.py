from User_UI import *
from Admin_UI import *
from Bank import *


def main():
    bank = Bank()

    while True:
        print("\n\n")
        print("#############################################")
        print("|  Welcome to the Banking Management System |")
        print("#############################################")
        print("1. User\n2. Admin\n3. Exit")

        user_type = input(
            "Are you a User or an Admin? Enter 1 for User, 2 for Admin, 3 to Exit: ")

        if user_type == '1':
            User_UI(bank=bank).user_menu()

        elif user_type == '2':
            Admin_UI(bank=bank).admin_menu()

        elif user_type == '3':
            print("Thank you for using our system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
