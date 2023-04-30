import sqlite3
from models import accountModel
import tkinter as tk

DATABASE = "atm.db"

class signInController:
    def __init__(self, view, session):
        self.view = view
        self.session = session

    def sign_In(self, username, password):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM ACCOUNT WHERE username = ?", [username]).fetchone()

        if data is None:
            self.view.no_user_label.pack(pady=5)
        elif (password == data[3]):
            # Initializes session with account data
            self.session.accountID = data[0]
            self.session.savingsID = cursor.execute("SELECT savingID FROM SAVING WHERE accountNum = ?", [self.session.accountID]).fetchone()[0]
            self.session.checkingID = cursor.execute("SELECT checkingID FROM CHECKING WHERE accountNum = ?", [self.session.accountID]).fetchone()[0]
            print(self.session)
            self.view.no_user_label.pack_forget()
            self.view.master.switch_to_user_accounts_screen(self.session)