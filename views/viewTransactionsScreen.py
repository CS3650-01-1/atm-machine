import tkinter as tk
from controllers.viewTransactionsController import viewTransactionsController

class ViewTransactions(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        # self.transaction_listbox = tk.Listbox(self, width=60, height=10)
        # self.transaction_listbox.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        # create headers for columns
        self.date_header = tk.Label(self, text="Date")
        self.date_header.grid(row=1, column=0, padx=5, pady=5)
        self.type_header = tk.Label(self, text="Type")
        self.type_header.grid(row=1, column=1, padx=5, pady=5)
        self.amount_header = tk.Label(self, text="Amount")
        self.amount_header.grid(row=1, column=2, padx=5, pady=5)

        # Retrieve transactions
        controller = viewTransactionsController(self, self.session)
        transactions = controller.get_all_transactions()
        # Display transactions
        for i, transaction in enumerate(transactions):
            self.date_label = tk.Label(self, text=transaction[5])
            self.date_label.grid(row=i+2, column=0, padx=5, pady=5)
            self.type_label = tk.Label(self, text=transaction[4])
            self.type_label.grid(row=i+2, column=1, padx=5, pady=5)
            self.amount_label = tk.Label(self, text=transaction[6])
            self.amount_label.grid(row=i+2, column=2, padx=5, pady=5)