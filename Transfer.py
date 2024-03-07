from Account import *
from Bank import *


class Transfer:
    @staticmethod
    def make_transfer(bank: Bank, from_account: Account, to_account_number: int, amount: int):
        if from_account.get_balance() < amount:
            return "Your balance is not sufficient to transfer"

        to_account: Account = bank.get_account(
            account_number=to_account_number)
        if (to_account == None):
            return "Account does not exist"

        from_account.transfer_money(account_id=to_account, amount=amount)
        to_account.recieve_money(
            account_id=from_account.get_account_number(), amount=amount)
        return "Transfer successfull"
