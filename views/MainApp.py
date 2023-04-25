import tkinter as tk
from accountCreationView import *
from confirmationCreationView import *
from homeView import *
from passwordCreationView import *
from transactionsView import *
from userAccountsView import *
from withdrawConfirmView import *
from withdrawView import *
from transferView import *
from transferConfirmationView import *
from checkBalanceView import*

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
        

    def switch_to_withdraw_screen(self):
        # Switch to withdraw screen
        self.withdraw_screen = WithdrawScreen(self)
        self.transactions_screen.pack_forget()
        self.withdraw_screen.pack()
        self.withdraw_confirm_screen = WithdrawConfirmScreen(self)
    
    def switch_to_withdraw_confirm_screen(self):
        # Switch to withdraw confirm screen
        self.withdraw_screen.pack_forget()
        self.withdraw_confirm_screen.pack()

    def switch_to_transfer_screen(self):
        # Switch to transfer screen
        self.transfer_screen = TransferScreen(self)
        self.transactions_screen.pack_forget()
        self.transfer_screen.pack()
        

    def switch_to_password_creation_screen(self):
        # Switch to password creation screen
        self.account_creation_screen.pack_forget()
        self.password_creation_screen.pack()
        self.confirm_creation_screen = ConfirmCreationScreen(self)

    def switch_to_confirmation_screen(self):
        # Switch to password confirm screen
        self.password_creation_screen.pack_forget()
        self.confirm_creation_screen.pack()

    def switch_to_home_screen_from_password(self):
        # Switch to home screen from password confirmation screen
        self.confirm_creation_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack()

    def switch_to_user_accounts_from_password_screen(self):
        # Switch to user accounts screen from password confirmation screen
        self.user_accounts_screen = UserAccounts(self)
        self.confirm_creation_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_user_accounts_from_withdraw_screen(self):
        # Switch to user accounts screen from withdraw confirmation screen
        self.user_accounts_screen = UserAccounts(self)
        self.withdraw_confirm_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_withdraw(self):
        # Switch to home screen from withdraw confirmation screen
        self.withdraw_confirm_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 

    def switch_to_transfer_confirm_screen(self):
        # Switch to transfer screen
        self.transfer_confirm_screen = ConfirmTransferScreen(self)
        self.transfer_screen.pack_forget()
        self.transfer_confirm_screen.pack()
    
    def switch_to_user_accounts_from_transfer_screen(self):
        # Switch to user accounts screen from transfer confirmation screen
        self.user_accounts_screen = UserAccounts(self)
        self.transfer_confirm_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_transfer(self):
        # Switch to home screen from transfer confirmation screen
        self.transfer_confirm_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 

    def switch_to_check_balance_screen(self):
        self.check_balance_screen = CheckBalance(self)
        self.transactions_screen.pack_forget()
        self.check_balance_screen.pack()

    def switch_to_user_accounts_from_check_balance_screen(self):
        # Switch to user accounts screen from transfer confirmation screen
        self.user_accounts_screen = UserAccounts(self)
        self.check_balance_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_check_balance(self):
        # Switch to home screen from transfer confirmation screen
        self.check_balance_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 



app = MainApp()
app.mainloop()