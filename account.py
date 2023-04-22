'''
class representing a bank account; its transaction log is done through database relation
'''

import sqlite3, secrets
from sqlite3 import Error
from atm import DATABASE

class Account:
    # probably irrelevant
    def __init__(self, pin, ownerID, accountNum=None):
        self.accountNum = accountNum or self.generate_id()
        self.pin = pin
        self.ownerID = ownerID

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
        cursor.execute("INSERT OR ABORT INTO ACCOUNT VALUES(?, ?, ?)", (self.accountNum, self.ownerID, self.pin))
        connection.commit()

    #"read"
    # unsure of how necessary the staticmethod annotation is
    @staticmethod
    def retrieve(accountNum):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM ACCOUNT WHERE accountNum = ?",[accountNum]).fetchone()
        return Account(data[2], data[1], accountNum=data[0])

    #"update"
    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO ACCOUNT VALUES(?, ?, ?)", (self.accountNum, self.ownerID, self.pin))
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

class Savings:
    def __init__(self,accountNum,accountBalance, savingsID=None):
        self.savingsID = savingsID or self.generate_id
        self.accountNum = accountNum
        self.accountBalance = accountBalance
    
    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5]) # fills 0's
            data = cursor.execute("SELECT savingsID FROM SAVING WHERE savingsID = ?",[id]).fetchone()
            if not data:
                return id

    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO SAVING VALUES(?, ?, ?)", (self.savingsID, self.accountNum, self.accountBalance))
        connection.commit()

    @staticmethod
    def retrieve(savingsID):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM SAVING WHERE savingID = ?",[savingsID]).fetchone()
        return Savings(data[1],data[2], savingsID=data[0])

    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO SAVING VALUES(?, ?, ?)", (self.savingsID, self.accountNum, self.accountBalance))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM SAVING WHERE savingID = ?", [self.savingsID])
        connection.commit()

    def __str__(self) -> str:
        return f"Savings ID: {self.savingsID}, master account number: {self.accountNum}, balance: {self.accountBalance}"

class Checking:
    def __init__(self,checkingID,accountNum,accountBalance):
        self.checkingID = checkingID
        self.accountNum = accountNum
        self.accountBalance = accountBalance
    
    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO CHECKING VALUES(?, ?, ?)", (self.checkingID, self.accountNum, self.accountBalance))
        connection.commit()

    @staticmethod
    def retrieve(checkingID):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT checkingID, accountNum, accountBalance FROM CHECKING WHERE checkingID = ?",[checkingID]).fetchone()
        return Checking(data[0],data[1],data[2])

    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO CHECKING VALUES(?, ?, ?)", (self.checkingID, self.accountNum, self.accountBalance))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM CHECKING WHERE checkingID = ?", [self.checkingID])
        connection.commit()

    def __str__(self) -> str:
        return f"Checking ID: {self.checkingID}, master account number: {self.accountNum}, balance: {self.accountBalance}"