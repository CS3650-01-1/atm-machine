from datetime import datetime
import sqlite3, secrets

DATABASE = "atm.db"

'''
class representing the log of a transaction
'''
class Transaction:
    def __init__(self, transactionType, amount, accountID, specificID, accountType, transaction_id=None, date=None):
        self.transactionType = transactionType
        self.date = date or datetime.now()    # log datetime on init
        self.amount = amount
        self.transaction_id = transaction_id or self.generate_id()
        self.accountID = accountID
        self.specificID = specificID
        self.accountType = accountType

    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5])
            data = cursor.execute("SELECT transactionID FROM TRANSACTIONS WHERE transactionID = ?",[id]).fetchone()
            if not data:
                return id

    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO TRANSACTIONS VALUES(?, ?, ?, ?, ?, ?, ?)", (self.transaction_id, self.accountID, self.specificID, self.accountType, self.transactionType, self.date, self.amount))
        connection.commit()

    @staticmethod
    def retrieve(transaction_id):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM TRANSACTIONS WHERE transactionID = ?",[transaction_id]).fetchone()
        if data:
            return Transaction(data[4], data[6], data[1], data[2], data[3], transaction_id=data[0], date=data[5])
        return None
    
    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO TRANSACTIONS VALUES (?, ?, ?, ?, ?, ?, ?)", (self.transaction_id, self.accountID, self.specificID, self.accountType, self.transactionType, self.date, self.amount))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM TRANSACTIONS WHERE transactionID = ?",[self.transaction_id])
        connection.commit()

    def __str__(self):  # something to print for future debugging
        # buncha objects so cant print until other str methods are done
        return f"Type: {self.transactionType}\nDate: {self.date}\nAmount: {self.amount}\nTransaction ID: {self.transaction_id}\nAccount ID: {self.accountID}"