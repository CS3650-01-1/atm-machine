import sqlite3
from models.personModel import *
from models.accountModel import *
import tkinter as tk

DATABASE = "atm.db"

def sign_In(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    data = cursor.execute("SELECT password FROM ACCOUNT WHERE username = ?", [username]).fetchone()
    print(data)
    session = {}

    if data is None:
        no_user_label = tk.Label( text = "Incorrect username")
        no_user_label.pack(pady=5)
    elif (password == data[0]):
        error_label = tk.Label(text="Wrong password \nPlease try again!")
        error_label.pack(pady=5)

