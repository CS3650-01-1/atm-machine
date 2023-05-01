import tkinter as tk
from controllers.depositController import depositController
from decimal import *

class DepositScreen(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.master = master
        self.session = session
        self.create_widgets()

    def create_widgets(self):
        # Create deposit screen label and prompt the user for the amount to deposit
        self.welcome_label = tk.Label(self, text="Please specify the amount\nyou are depositing", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=10)

        # Create Amount label
        self.amount_label = tk.Label(self, text="Amount to deposit:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # Create button to submit deposit and go back to the main menu
        submit_button = tk.Button(self, text="Deposit", command=self.submit_deposit)
        submit_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.back_button_pressed)
        self.back_button.pack(side="bottom", pady=5)

        self.error_label = tk.Label(self, text="Enter a valid dollar amount!")

    def back_button_pressed(self):
        self.master.switch_to_trans_screen(self, self.session)

    def submit_deposit(self):
        # validate input
        entered_string = self.amount_entry.get()
        try:
            if '.' in entered_string and len(entered_string.split('.')[1]) > 2:
                print(entered_string.split('.')[1])
                raise InvalidOperation
            decimalEntry = Decimal(entered_string)
            depo = depositController(self, self.session)
            if(depo.submit_deposit(decimalEntry) is False):
                raise InvalidOperation
            self.master.switch_to_deposit_confirmation_screen(self.session)
        except InvalidOperation:
            self.error_label.pack_forget()
            self.error_label.pack(pady=10)




