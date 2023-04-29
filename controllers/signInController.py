import sqlite3
from models import accountModel
import tkinter as tk

DATABASE = "atm.db"

class signInController:
    def __init__(self, view):
        self.view = view

    def sign_In(self, username, password):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT password FROM ACCOUNT WHERE username = ?", [username]).fetchone()
        session = {}

        if data is None:
            no_user_label = tk.Label( text = "Incorrect username or password")  # this doesnt check password 
            no_user_label.pack(pady=5)
        elif (password == data[0]):
            self.view.master.switch_to_user_accounts_screen()