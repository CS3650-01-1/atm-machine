'''
class representing a bank account; its transaction log is done through database relation
'''

import sqlite3, secrets
from sqlite3 import Error

DATABASE = "atm.db"

class Account:
    def __init__(self, name, username, password, email, phone, address, accountNum=None):
        self.accountNum = accountNum or self.generate_id()
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
        

    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5]) # fills 0's
            data = cursor.execute("SELECT accountNum FROM ACCOUNT WHERE accountNum = ?",[id]).fetchone()
            if not data:
                return id

    # "create"
    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO ACCOUNT VALUES(?, ?, ?, ?, ?, ?, ?)", (self.accountNum, self.name, self.username, self.password, self.email, self.phone, self.address))
        connection.commit()

    #"read"
    # unsure of how necessary the staticmethod annotation is
    @staticmethod
    def retrieve(accountNum):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM ACCOUNT WHERE accountNum = ?",[accountNum]).fetchone()
        return Account(data[1], data[2], data[3], data[4], data[5], data[6], accountNum=data[0])

    #"update"
    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO ACCOUNT VALUES(?, ?, ?, ?, ?, ?, ?)", (self.accountNum, self.name, self.username, self.password, self.email, self.phone, self.address))
        connection.commit()

    #"delete"
    # ...probably not necessary? but it is here for completion's sake anyway
    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ACCOUNT WHERE accountNum = ?", [self.accountNum])
        connection.commit()

    def __str__(self):
        return f"Account ID: {self.accountNum}"



