import sqlite3
import tkinter as tk
from models.atm import ATM

class checkBalanceController:
    def __init__(self, view, session):
        self.view = view
        self.session = session

    def getBalance(self):
        if self.session.accountType == "savings":
            return ATM.check_balance(ATM, self.session.savingsID, self.session.accountType)
        elif self.session.accountType == "checking":
            return ATM.check_balance(ATM, self.session.checkingID, self.session.accountType)
