import sqlite3

from models import atm
from views.depositView import *
from models.atm import ATM
DATABASE = "atm.db"

class depositController:
    def __init__(self, view, session):
        self.view = view
        self.session = session
        
    def submit_deposit(self, amount):
        if self.session.accountType == "savings":
            return ATM.deposit_cash( ATM, amount, self.session.savingsID, self.session.accountID, self.session.accountType)
        elif self.session.accountType == "checking":
            return ATM.deposit_cash(ATM, amount, self.session.checkingID, self.session.accountID, self.session.accountType)


