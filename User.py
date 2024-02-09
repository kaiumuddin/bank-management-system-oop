class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.__account_number = None
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__balance = 0
        self.__transactions = []
    
    def deposit(self, money):
        self.__balance += money
        self.__make_transaction(tname="Deposit", amount=money)

    def withdrawal(self, money):
        if money > self.__balance:
            return False
        
        self.__balance -= money
        self.__make_transaction(tname="Withdrawal", amount=money)
        return True

    def get_balance(self):
        return self.__balance

    def __make_transaction(self, tname, amount):
        self.__transactions.append(f"{tname} : {amount}")
    
    def get_transactions_history(self):
        return self.__transactions;

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f'{cls}:: Account Number:{self.__account_number}, name:{self.__name}, email:{self.__email}, balance:{self.__balance}'
