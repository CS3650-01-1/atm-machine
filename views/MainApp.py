import tkinter as tk
from accountCreationView import *
from confirmationCreationView import *
from homeView import *
from passwordCreationView import *
from transactionsView import *
from userAccountsView import *
from withdrawConfirmView import *
from withdrawView import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create homescreen on startup 
        self.title("ATM System")
        self.geometry("800x400")
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack()

    def switch_to_account_creation_screen(self):
        # Switch to account creation screen
        self.home_screen.pack_forget()
        self.account_creation_screen.pack()
        self.password_creation_screen = PasswordCreationScreen(self)

    def switch_to_user_accounts_screen(self):
        # Switch to user accounts screen
        self.user_accounts_screen = UserAccounts(self)
        self.home_screen.pack_forget()
        self.user_accounts_screen.pack()
        self.transactions_screen = Transactions(self)
    
    def switch_to_transactions_screen(self):
        # Switch to transactions screen
        self.user_accounts_screen.pack_forget()
        self.transactions_screen.pack()
        self.withdraw_screen = WithdrawScreen(self)

    def switch_to_withdraw_screen(self):
        # Switch to withdraw screen
        self.transactions_screen.pack_forget()
        self.withdraw_screen.pack()
        self.withdraw_confirm_screen = WithdrawConfirmScreen(self)
    
    def switch_to_withdraw_confirm_screen(self):
        # Switch to withdraw confirm screen
        self.withdraw_screen.pack_forget()
        self.withdraw_confirm_screen.pack()

    def switch_to_password_creation_screen(self):
        # Switch to password creation screen
        self.account_creation_screen.pack_forget()
        self.password_creation_screen.pack()
        self.confirm_creation_screen = ConfirmCreationScreen(self)

    def switch_to_confirmation_screen(self):
        # Switch to password confirm screen
        self.password_creation_screen.pack_forget()
        self.confirm_creation_screen.pack()



app = MainApp()
app.mainloop()