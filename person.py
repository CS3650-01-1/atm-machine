'''
class representing a person; acts as a "master" account to multiple bank accounts
'''

import secrets
import sqlite3

DATABASE = "atm.db"

class Person:
    def __init__(self, first_name, last_name, email_address, telephone_number, physical_address, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.telephone_number = telephone_number
        self.physical_address = physical_address
        self.id = id or self.generate_id() 

    def generate_id(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        while True:
            gen_id = secrets.randbelow(100000)  # generate int from 0 to 99999
            id = int(str(gen_id).rjust(5, '0')[:5])
            data = cursor.execute("SELECT personID FROM PERSON WHERE personID = ?",[id]).fetchone()
            if not data:
                return id

    def create_in_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR ABORT INTO PERSON VALUES(?, ?, ?, ?, ?, ?)", (self.id, self.first_name, self.last_name, self.email_address, self.telephone_number, self.physical_address))
        connection.commit()

    @staticmethod
    def retrieve(id):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM PERSON WHERE personID = ?",[id]).fetchone()
        if data:
            return Person(data[1], data[2], data[3], data[4], data[5], id=data[0])
        return None
    
    def update_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO PERSON VALUES(?, ?, ?, ?, ?, ?)", (self.id, self.first_name, self.last_name, self.email_address, self.telephone_number, self.physical_address))
        connection.commit()

    def delete_from_db(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM PERSON WHERE personID = ?",[self.id])
        connection.commit()

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nEmail: {self.email_address}\nPhone: {self.telephone_number}\nAddress: {self.physical_address}"