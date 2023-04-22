'''
class representing the ATM interface; all actions that the user can do are done through this class
'''
import sqlite3
from sqlite3 import Error

from account import *

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
        data = cursor.execute("SELECT * FROM ATM WHERE atmID = ?",[atmID]).fetchone()
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

    def authenticate_pin(account_number, pin) -> bool:
        Account
        if data is None:
            return False
        return True

    def deposit_cash(self, amount, account_number, account_type):
        if account_type == "checking":
            account = Checking.retrieve(account_number)
            account.addBalance(amount)
            account.update_db()
        elif account_type == "savings":
            account = Savings.retrieve(account_number)
            account.addBalance(amount)
            account.update_db()
        self.cash_available += amount
        self.update_db()

    def deposit_check(amount, account_number, account_type):
        pass

    def withdraw_cash(amount, account_number, account_type):
        # deny withdrawal if not enough balance
        pass

    def transfer_balance(amount, account_number):
        # deny transfer if not enough balance
        pass

    def check_balance(account_number, account_type):
        pass

