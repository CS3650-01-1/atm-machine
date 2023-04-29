import sqlite3
import tkinter as tk
from models.checkingsModel import Checking

class checkBalanceController:
    def __init__(self, view, session):
        self.view = view
        self.session = session

    def getBalance(self):
        account = Checking.retrieve(self.session.checkingID)
        return account.accountBalance