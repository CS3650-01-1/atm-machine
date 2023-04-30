import tkinter as tk
from controllers.viewTransactionsController import viewTransactionsController

class ViewTransactions(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.transaction_listbox = tk.Listbox(self)
        self.transaction_listbox.pack(side="top", pady=10)

        # Retrieve transactions
        controller = viewTransactionsController(self, self.session)
        transactions = controller.get_all_transactions()
        # Display transactions
        for transaction in transactions:
            self.transaction_listbox.insert(tk.END, "Date: {}\tTransaction Type: {}\tAmount: {}".format(transaction[5], transaction[4], transaction[6]))
        pass