from User_Interface import *
from Admin_Interface import *
from Bank import *
from Admin import *

def main():
    bank = Bank()    


    while True:
        print("\nWelcome to the Banking Management System")
        print("1. User\n2. Admin\n3. Exit")

        user_type = input(
            "Are you a User or an Admin? Enter 1 for User, 2 for Admin, 3 to Exit: ")

        if user_type == '1':
            user_interface = User_Interface(bank=bank, account=None)
            user_interface.user_menu()

        elif user_type == '2':
            admin_interface = Admin_Interface(admin=None, bank=bank)
            admin_interface.admin_menu()

        elif user_type == '3':
            print("Thank you for using our system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            


if __name__ == "__main__":
    main()
