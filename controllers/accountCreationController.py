import sqlite3
from models import accountModel
from views import accountCreationView
DATABASE = "atm.db"

class AccountCreationController:
    def __init__(self, view):
        self.view = view

    def submit_account(self, full_name, username, password, email_address, telephone_number, physical_address):
        # validation
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        if not cursor.execute("SELECT username FROM ACCOUNT WHERE username = ?", [username]).fetchone() is None:
            self.view.hide_error_labels()
            self.view.username_taken_error_label.pack(pady=10)

            return
        all_fields_valid = True

        # ensure all fields have valid input here
        # I realize that I wrote this all out and there are so many better ways to do this
        # but if it works it works, right?

        # full name
        if len(full_name) == 0:
            all_fields_valid = False
        
        # password
        if len(password) == 0:
            all_fields_valid = False

        # email address
        if len(email_address) == 0:
            all_fields_valid = False

        # telephone number
        if len(telephone_number) == 0:
            all_fields_valid = False

        # physical address    
        if len(physical_address) == 0:
            all_fields_valid = False
        
        if not all_fields_valid:
            self.view.hide_error_labels()
            self.view.invalid_field_inputs_error_label.pack(pady=10)
            return
        else:
            account = accountModel.Account(full_name, username, password, email_address, telephone_number, physical_address)
            account.create_in_db()
            #self.view.master.switch_to_home_view()
            self.view.master.switch_to_confirmation_from_creation_view(self.view)


