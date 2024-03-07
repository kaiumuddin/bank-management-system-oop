class Bank:
    def __init__(self) -> None:
        self.__accounts = {}
        self.__loan_feature = True
        self.__total_loan = 0
        self.__total_balance = 0

    def create_account(self, account):
        account_number = len(self.__accounts) + 100
        account.set_account_number(account_number)
        self.__accounts[account_number] = account
        return account

    def get_account(self, account_number, email=None):
        if account_number in self.__accounts:
            account = self.__accounts[account_number]
            if email == None:
                return account
            if email and account.get_email() == email:
                return account
            else:
                return None
        else:
            return None

    def delete_account(self, account):
        if account and account.get_account_number() in self.__accounts:
            del self.__accounts[account.get_account_number()]
            print("Account deleted successfully")
        else:
            print("No account found")

    def get_all_accounts(self):
        return self.__accounts.items()

    def get_total_balance(self):
        return self.__total_balance

    def increase_total_balance(self, amount):
        self.__total_balance += amount

    def decrease_total_balance(self, amount):
        self.__total_balance -= amount

    def get_loan_amount(self):
        return self.__total_loan

    def get_loan_feature(self):
        return self.__loan_feature

    def set_loan_feature(self, value):
        self.__loan_feature = value

    def increase_total_loan(self, amount):
        self.__total_loan += amount

    def decrease_total_loan(self, amount):
        self.__total_loan -= amount
