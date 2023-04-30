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

        self.error_label = tk.Label(self, text="Enter a valid dollar amount!")


    def submit_deposit(self):
        # validate input
        entered_string = self.amount_entry.get()
        if not (entered_string.isdecimal()):
            self.error_label.pack(pady=10)
        else:
            depo = depositController(self, self.session)
        # convert the entered string to a Decimal object, and then rounds it to two decimal places;
        # then pass the value to the controller
            depo.submit_deposit(round(Decimal(self.amount_entry.get()),2))
            #Go back to home screen
            self.master.switch_to_deposit_confirmation_screen(self.session)




