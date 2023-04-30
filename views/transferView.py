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

    def transfer_submit_clicked(self):
        controller = transferBalanceController(self, self.session)
        controller.transferBalance(round(Decimal(self.amount_entry.get()),2))
        self.master.switch_to_transfer_confirm_screen(self.session)
