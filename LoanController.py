from Bank import *
from Account import *


class LoanController:
    def createLoan(self, bank: Bank, account: Account, loan_amount: int):
        if bank.get_total_balance() < loan_amount:
            return "Bank is bankrupt"
        if account.allowed_to_take_loan() == True and bank.get_loan_feature() == True:
            bank.increase_total_loan(loan_amount)
            account.take_loan(loan_amount)
            account.make_transaction(tname="Loan taken", amount=loan_amount)
            return "Loan taken"
        else:
            return "Loan feature is off"
