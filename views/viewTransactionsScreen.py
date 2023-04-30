from datetime import datetime
import tkinter as tk
from tkinter import ttk
from controllers.viewTransactionsController import viewTransactionsController

class ViewTransactions(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        # ready the treeview for transactions
        self.transaction_treeview = ttk.Treeview(self)
        self.transaction_treeview['columns'] = ('date', 'type', 'amount')
        self.transaction_treeview.heading('#0', text='', anchor='w')
        self.transaction_treeview.heading('date', text='Date', anchor='w')
        self.transaction_treeview.heading('type', text='Type', anchor='w')
        self.transaction_treeview.heading('amount', text='Amount', anchor='w')
        self.transaction_treeview.column('#0', width=0, stretch=tk.NO)
        self.transaction_treeview.column('date', width=180, anchor='w')
        self.transaction_treeview.column('type', width=180, anchor='w')
        self.transaction_treeview.column('amount', width=180, anchor='w')

        # create scrollbar and attach to treeview
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.transaction_treeview.yview)
        self.transaction_treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')

        # retrieve transactions
        controller = viewTransactionsController(self, self.session)
        transactions = controller.get_all_transactions()

        # display transactions
        for i, transaction in enumerate(transactions):
            date_str = datetime.fromisoformat(transaction[5]).strftime('%m/%d/%Y - %H:%M')
            self.transaction_treeview.insert('', tk.END, text='', values=(date_str, transaction[4], transaction[6]))

        # pack treeview
        self.transaction_treeview.pack(side='top', fill='both', expand=True)

        # create back button
        self.back_button = tk.Button(self, text='Back', command=self.back_clicked)
        self.back_button.pack(side='bottom', padx=10, pady=10)

        self.pack(fill='both', expand=True, padx=20, pady=20)

    def back_clicked(self):
        self.master.switch_to_transaction_from_view_screen(self.session)
