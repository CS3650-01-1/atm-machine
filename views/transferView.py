import tkinter as tk

from controllers.transferBalanceController import transferBalanceController
from decimal import *


class TransferScreen(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self, text="Enter amount to transfer into other account:", font=("Arial", 18))
        self.welcome_label.pack(side="top", pady=10)

        # Create an entry for the amount input
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady = 10)

        # Create a submit button
        submit_button = tk.Button(self, text="Submit", command=self.transfer_submit_clicked)
        submit_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.back_button_pressed)
        self.back_button.pack(side="bottom", pady=5)

        # Create error label
        self.error_label = tk.Label(self, text="Insufficient funds or invalid input! Please try a different amount.")

    def back_button_pressed(self):
        self.master.switch_to_trans_screen(self, self.session)

    def transfer_submit_clicked(self):
        # validate input
        entered_string = self.amount_entry.get()
        try:
            if '.' in entered_string and len(entered_string.split('.')[1]) > 2:
                print(entered_string.split('.')[1])
                raise InvalidOperation
            decimalEntry = Decimal(entered_string)
            controller = transferBalanceController(self, self.session)
            if(controller.transferBalance(decimalEntry) is False):
                raise InvalidOperation
            self.master.switch_to_transfer_confirm_screen(self.session)
        except InvalidOperation:
            self.error_label.pack_forget()
            self.error_label.pack(pady=10)
