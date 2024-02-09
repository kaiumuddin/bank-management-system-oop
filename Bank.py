class Bank:
    def __init__(self) -> None:
        self.accounts = {}
        self.admins = {}
        self.loan_feature = True
        self.loan = 0

    def get_loan_amount(self, admin):
        if admin.id in self.admins:
            return self.loan
        return -1

    def get_loan_feature(self, admin):
        if admin.id in self.admins:
            return self.loan_feature
        return -1

    def set_loan_feature(self, admin, value):
        if admin.id in self.admins:
            self.loan_feature = value

    def create_admin(self, admin):
        admin.id = len(self.admins) + 1
        self.admins[admin.id] = admin
        print(f"Created {admin}")
    
    def get_admin(self, id):
        admin = self.admins[id]
        return admin

    def create_account(self, account):
        account.account_number = len(self.accounts) + 100
        self.accounts[account.account_number] = account
        print(f"Created  {account}")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def delete_account(self, admin, account):
        if admin.id in self.admins:
            if account.account_number in self.accounts:
                del self.accounts[account.account_number]
            else:
                print("No account found")
        else:
            print("Admin is not authorized")

    def get_all_accounts(self, admin):
        if admin.id in self.admins:
            return self.accounts.items()

    def get_total_balance(self, admin):
        if admin.id in self.admins:
            balance = 0
            for account_number, user in self.accounts.items():
                balance += user.get_balance()
            return balance
        return -1












# admin = Admin(name="admin", email="admin@gmail.com", password="admin")
# user = User(name="Kaium Uddin", email="kaium@gmail.com",
#             address="Dhaka", account_type="savings")
# bank.create_account(user)
# bank.create_admin(admin)
# # bank.delete_account(admin, user);

# print(bank.get_account(user.account_number))
# print("Balance = ", bank.get_total_balance(admin=admin))
