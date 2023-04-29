import sqlite3

from models.atm import ATM

DATABASE = "atm.db"
class withdrawController:
    def __init__(self, view, session):
        self.view = view
        self.session = session
    def submit_withdraw(self, amount):
        if self.session.accountType == "savings":
            return ATM.withdraw_cash(ATM, amount, self.session.savingsID, self.session.accountID,self.session.accountType)
        elif self.session.accountType == "checking":
            return ATM.withdraw_cash(ATM,amount, self.session.checkingID, self.session.accountID,self.session.accountType)
