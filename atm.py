'''
class representing the ATM interface; all actions that the user can do are done through this class
'''
from transaction import Transaction

class ATM:
    def __init__(self, location, card_available):
        self.location = location
        self.card_available = card_available

    def create_transaction(self, type,amount, account_number):
        id = "0000000"  # VERY TEMP, need to figure out ID generation
        transaction = Transaction(type, amount, id, account_number)
        transaction.save()

    def authenticate_pin(card_number, pin) -> bool:
        pass

    def deposit_cash(amount) -> Transaction:
        pass

    def deposit_check(amount) -> Transaction:
        pass

    def withdraw_cash(amount) -> Transaction:
        # deny withdrawal if not enough balance
        pass

    def transfer_balance(amount, account_number) -> Transaction:
        # deny transfer if not enough balance
        pass

    def check_balance():
        pass

