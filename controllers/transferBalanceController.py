import sqlite3
import tkinter as tk
from models.atm import ATM

DATABASE = "atm.db"

class transferBalanceController:
    def __init__(self, view, session):
        self.view = view
        self.session = session

    def transferBalance(self, amount):
        if self.session.accountType == "checking":
            return ATM.transfer_balance(ATM, amount, self.session.checkingID, self.session.savingsID, self.session.accountID, self.session.accountType)
        elif self.session.accountType == "savings":
            return ATM.transfer_balance(ATM, amount, self.session.savingsID, self.session.checkingID, self.session.accountID, self.session.accountType)
