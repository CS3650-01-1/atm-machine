import sqlite3
from models import personModel
from views import accountCreationView
DATABASE = "atmdb"



def submit_account(full_name, username, password, email_address, telephone_number, physical_address):
    
    account = personModel.Person(full_name,username, password,email_address, telephone_number, physical_address)
    account.create_in_db()


