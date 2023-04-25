import sqlite3, secrets
from sqlite3 import Error

DATABASE = "atm.db"

class Checking:
    def __init__(self,accountNum,accountBalance, checkingID=None):
        self.checkingID = checkingID or self.generate_id()
        self.accountNum = accountNum
        self.accountBalance = accountBalance

    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5]) # fills 0's
            data = cursor.execute("SELECT checkingID FROM CHECKING WHERE checkingID = ?",[id]).fetchone()
            if not data:
                return id
    
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
        return Checking(data[1],data[2], checkingID=data[0])

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

    def addBalance(self, amount):
        self.accountBalance += amount
        self.update_db()

    def removeBalance(self, amount):
        if self.accountBalance >= amount:
            self.accountBalance -= amount
            self.update_db()
        else:
            print("Insufficient funds")

    def __str__(self) -> str:
        return f"Checking ID: {self.checkingID}, master account number: {self.accountNum}, balance: {self.accountBalance}"