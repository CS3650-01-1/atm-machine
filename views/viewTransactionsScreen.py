import tkinter as tk
class ViewTransactions(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()
    
    def create_widgets():
        # Retrieve transactions

        # Display transactions

        pass