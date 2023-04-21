'''
class representing a bank account; its transaction log is done through database relation
'''

import sqlite3
from sqlite3 import Error
from atm import DATABASE

class Account:
    # probably irrelevant
    def __init__(self, accountNum, pin, ownerID):
        self.accountNum = accountNum
        self.pin = pin
        self.ownerID = ownerID

    # "create"
    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO ACCOUNT VALUES(?, ?, ?)", (self.accountNum, self.ownerID, self.pin))
        connection.commit()

    #"read"
    @staticmethod
    def retrieve(accountNum):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT accountNum, personID, pinNum FROM ACCOUNT WHERE accountNum = ?",[accountNum]).fetchone()
        return Account(data[0],data[2],data[1])

    #"update"
    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO ACCOUNT VALUES(?, ?, ?)", (self.accountNum, self.ownerID, self.pin))
        connection.commit()

    #"delete"
    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ACCOUNT WHERE accountNum = ?", [self.accountNum])
        connection.commit()

    def __str__(self):
        return f"Account ID: {self.accountNum}"

class Savings:
    pass

class Checking:
    pass