import tkinter as tk
from controllers.withdrawController import withdrawController
from decimal import *

class WithdrawScreen(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.master = master
        self.session = session
        self.create_widgets()


    def create_widgets(self):
        # Create welcome labels 
        self.welcome_label = tk.Label(self, text="Please enter the amount\nto withdraw", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=20)

        # Create Amount label
        self.amount_label = tk.Label(self, text="Amount: $")
        self.amount_label.pack(side="left")

        # Create Amount entry
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="left")

        # Create submit button
        submit_button = tk.Button(self, text="Submit", command=self.withdraw_submit_clicked)
        submit_button.pack(pady=5)

        self.error_label = tk.Label(self, text="Enter a valid dollar amount!")

    def withdraw_submit_clicked(self):
        # validate input
        entered_string = self.amount_entry.get()
        if not (entered_string.isdecimal()):
            self.error_label.pack(pady=10)
        else:
            # Switch to withdraw confirm screen
            controller = withdrawController(self, self.session)
            controller.submit_withdraw(round(Decimal(self.amount_entry.get()),2))
            self.master.switch_to_withdraw_confirm_screen(self.session)