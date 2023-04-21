'''
class representing the ATM interface; all actions that the user can do are done through this class
'''
from transaction import Transaction
import sqlite3
from sqlite3 import Error

DATABASE = "atm.db"

class ATM:
    def __init__(self, atm_id, location, cash_available):
        self.atm_id = atm_id
        self.location = location
        self.cash_available = cash_available

    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO ATM VALUES(?, ?, ?)", (self.atm_id, self.location, self.cash_available))
        connection.commit()

    @staticmethod
    def retrieve(atmID):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT atmID, location, cashAvailable FROM ATM WHERE atmID = ?",[atmID]).fetchone()
        return ATM(data[0],data[1],data[2])

    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO ATM VALUES(?, ?, ?)", (self.atm_id, self.location, self.cash_available))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ATM WHERE atmID = ?", [self.atm_id])
        connection.commit()

    def create_transaction(self, type,amount, account_number):
        id = "0000000"  # VERY TEMP, need to figure out ID generation
        transaction = Transaction(type, amount, id, account_number)
        transaction.save()

    def authenticate_pin(card_number, pin) -> bool:
        pass

    def deposit_cash(amount, account_number) -> Transaction:
        pass

    def deposit_check(amount, account_number) -> Transaction:
        pass

    def withdraw_cash(amount, account_number) -> Transaction:
        # deny withdrawal if not enough balance
        pass

    def transfer_balance(amount, account_number) -> Transaction:
        # deny transfer if not enough balance
        pass

    def check_balance(account_number):
        pass

