import sqlite3, secrets
from sqlite3 import Error
from decimal import *

DATABASE = "atm.db"

class Savings:
    def __init__(self,accountNum,accountBalance, savingsID=None):
        self.savingsID = savingsID or self.generate_id()
        self.accountNum = accountNum
        self.accountBalance = accountBalance
    
    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5]) # fills 0's
            data = cursor.execute("SELECT savingID FROM SAVING WHERE savingID = ?",[id]).fetchone()
            if not data:
                return id

    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO SAVING VALUES(?, ?, ?)", (self.savingsID, self.accountNum, str(self.accountBalance)))
        connection.commit()

    @staticmethod
    def retrieve(savingsID):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM SAVING WHERE savingID = ?",[savingsID]).fetchone()
        return Savings(data[1],Decimal(data[2]), savingsID=data[0])

    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO SAVING VALUES(?, ?, ?)", (self.savingsID, self.accountNum, str(self.accountBalance)))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM SAVING WHERE savingID = ?", [self.savingsID])
        connection.commit()

    def addBalance(self, amount):
        if amount > 0:
            self.accountBalance += amount
            self.update_db()
            return True
        else:
            return False

    def removeBalance(self, amount):
        if self.accountBalance >= amount:
            self.accountBalance -= amount
            self.update_db()
            return True
        else:
            print("Insufficient funds")
            return False


    def __str__(self) -> str:
        return f"Savings ID: {self.savingsID}, master account number: {self.accountNum}, balance: {self.accountBalance}"