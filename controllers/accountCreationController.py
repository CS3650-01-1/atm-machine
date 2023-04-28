import sqlite3
from personModel import *
from accountCreationView import *

DATABASE = "atm.db"
def submit_account(full_name, username, password, email_address, telephone_number, physical_address):
    # Create a new Person object with the given data
    person = Person(full_name.get(), username.get(), password.get(), email_address.get(), telephone_number.get(), physical_address.get())

    # Insert the person into the database
    person.create_in_db()
