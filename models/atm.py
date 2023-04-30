'''
class representing the ATM interface; all actions that the user can do are done through this class
'''
import sqlite3
from sqlite3 import Error

from .accountModel import *
from .checkingsModel import *
from .savingsModel import *
from .transaction import *

DATABASE = "atm.db"

class ATM:
    def __init__(self, atm_id, location, cash_available):
        # self.atm_id = atm_id
        # self.location = location
        # self.cash_available = cash_available
        pass

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
        account = Account.retrieve(account_number)
        if account[0] == pin:
            return True
        return False

    def deposit_cash(self, amount, specific_id, account_id, account_type):
        if account_type == "checking":
            account = Checking.retrieve(specific_id)
            account.addBalance(amount)
            account.update_db()
        elif account_type == "savings":
            account = Savings.retrieve(specific_id)
            account.addBalance(amount)
            account.update_db()
        # self.cash_available += amount
        #self.update_db()
        self.log_transaction(self, "deposit", amount, specific_id, account_id, account_type)

    # we can probably get rid of this and just make a catch-all deposit method
    def deposit_check(self, amount, specific_id, account_id, account_type):
        if account_type == "checking":
            account = Checking.retrieve(specific_id)
            account.addBalance(amount)
            account.update_db()
        elif account_type == "savings":
            account = Savings.retrieve(specific_id)
            account.addBalance(amount)
            account.update_db()
        self.log_transaction("deposit", amount, specific_id, account_id, account_type)

    def withdraw_cash(self, amount, specific_id, account_id, account_type):
        if account_type == "checking":
            account = Checking.retrieve(specific_id)
            account.removeBalance(amount)
            account.update_db()
            #self.cash_available -= amount
        elif account_type == "savings":
            account = Savings.retrieve(specific_id)
            account.removeBalance(amount)
            account.update_db()
           # self.cash_available -= amount
        #self.update_db()
        self.log_transaction(self, "withdraw", amount, specific_id, account_id, account_type)

    def transfer_balance(self, amount, source_id, destination_id, account_id, account_type):
        # deny transfer if not enough balance
        if account_type == "checking":
            source_account = Checking.retrieve(source_id)
            destination_account = Savings.retrieve(destination_id)
            source_account.removeBalance(amount)
            destination_account.addBalance(amount)
        elif account_type == "savings":
            source_account = Savings.retrieve(source_id)
            destination_account = Checking.retrieve(destination_id)
            source_account.removeBalance(amount)
            destination_account.addBalance(amount)
        self.log_transaction(self, "Transfer", amount, source_id, account_id, account_type)

    def check_balance(self, specific_id, account_type):
        if account_type == "checking":
            account = Checking.retrieve(specific_id)
            balance = account.accountBalance
            return balance
        elif account_type == "savings":
            account = Savings.retrieve(specific_id)
            balance = account.accountBalance
            return balance

    def log_transaction(self, type, amount, specific_id, account_id, account_type):
        # create transaction object and create in db
        transaction = Transaction(type, amount, account_id, specific_id, account_type)
        transaction.create_in_db()

    def get_all_transactions(self, specific_id):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM TRANSACTIONS WHERE specificID = ?", [specific_id]).fetchall()

        return data
