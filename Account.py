class Account:
    def __init__(self, name, email, address, account_type) -> None:
        self.__account_number = None
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__balance = 0
        self.__transactions = []
        self.__loan = 0
        self.__loan_taken = 0

    def get_email(self):
        return self.__email

    def deposit(self, money):
        self.__balance += money
        self.make_transaction(tname="Deposit", amount=money)

    def withdrawal(self, money):
        if money > self.__balance:
            return False

        self.__balance -= money
        self.__make_transaction(tname="Withdrawal", amount=money)
        return True

    def transfer_money(self, account_id: int, amount: int):
        self.__balance -= amount
        self.make_transaction(
            f"Transfered to {account_id}", amount=amount)

    def recieve_money(self, account_id: int, amount: int):
        self.__balance += amount
        self.make_transaction(
            f"Recieved from {account_id}", amount=amount)

    def set_account_number(self, id):
        self.__account_number = id

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def make_transaction(self, tname, amount):
        self.__transactions.append(f"{tname} : {amount}")

    def get_transactions_history(self):
        return self.__transactions

    def take_loan(self, amount):
        if self.allowed_to_take_loan():
            self.__loan += amount
            self.__loan_taken += 1
            self.__balance += amount
            return True
        return False

    def allowed_to_take_loan(self):
        return self.__loan_taken < 2

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f'{cls}::\n Account Number:{self.__account_number},\nname:{self.__name}, \nemail:{self.__email}, \nbalance:{self.__balance}'
