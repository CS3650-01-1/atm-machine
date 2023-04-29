import sqlite3
from models.personModel import *
from models.accountModel import *
import tkinter as tk

DATABASE = "atm.db"

def sign_In(self, username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    data = cursor.execute("SELECT password FROM ACCOUNT WHERE username = ?", [username]).fetchone()

    session = {}
    if data is None:
        self.no_user_label = tk.Label(self, text = "Incorrect username")
        self.no_user_label.pack(pady=5)
    elif (password == data[0]):
        self.error_label = tk.Label(self, text="Wrong password \nPlease try again!")
        self.error_label.pack(pady=5)
    else :
        self.master.switch_to_user_accounts_screen()