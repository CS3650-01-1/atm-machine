import tkinter as tk
from views.accountCreationView import *
from views.homeView import *
from views.confirmationCreationView import *
from views.passwordCreationView import *
from views.transactionsView import *
from views.userAccountsView import *
from views.withdrawConfirmView import *
from views.withdrawView import *
from views.transferView import *
from views.transferConfirmationView import *
from views.checkBalanceView import *
from views.depositView import *
from views.depositConfirmationView import *
from views.viewTransactionsScreen import *

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

    def switch_to_user_accounts_screen(self, session):
        # Switch to user accounts screen
        self.user_accounts_screen = UserAccounts(session, master=self)
        self.home_screen.pack_forget()
        self.user_accounts_screen.pack()
    
    def switch_to_transactions_screen(self, session):
        # Switch to transactions screen
        self.transactions_screen = Transactions(session, master=self)
        self.user_accounts_screen.pack_forget()
        self.transactions_screen.pack()

    def switch_to_view_trans_screen(self, session):
        self.view_trans_screen = ViewTransactions(session, master=self)
        self.transactions_screen.pack_forget()
        self.view_trans_screen.pack()

    def switch_to_deposit_screen(self, session):
        # Switch to deposit screen 
        self.deposit_screen = DepositScreen(session, master=self)
        self.transactions_screen.pack_forget()
        self.deposit_screen.pack()

    def switch_to_deposit_confirmation_screen(self, session):
        # Switch to deposit confirmation screen
        self.deposit_confirmation_screen = DepositCreationScreen(session, master=self)
        self.deposit_screen.pack_forget()
        self.deposit_confirmation_screen.pack()
    
    def switch_to_user_accounts_from_deposit_screen(self, session):
        # Switch to user accounts screen from deposit screen
        self.user_accounts_screen = UserAccounts(session, master = self)
        self.deposit_confirmation_screen.pack_forget()
        self.user_accounts_screen.pack()
    
    def switch_to_home_screen_from_deposit(self):
        # Switch to home screen from withdraw confirmation screen
        self.deposit_confirmation_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 
        

    def switch_to_withdraw_screen(self, session):
        # Switch to withdraw screen
        self.withdraw_screen = WithdrawScreen(session, master=self)
        self.transactions_screen.pack_forget()
        self.withdraw_screen.pack()

    
    def switch_to_withdraw_confirm_screen(self, session):
        # Switch to withdraw confirm screen
        self.withdraw_confirm_screen = WithdrawConfirmScreen(session, master = self)
        self.withdraw_screen.pack_forget()
        self.withdraw_confirm_screen.pack()

    def switch_to_transfer_screen(self, session):
        # Switch to transfer screen
        self.transfer_screen = TransferScreen(session, master=self)
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

    def switch_to_user_accounts_from_withdraw_screen(self, session):
        # Switch to user accounts screen from withdraw confirmation screen
        self.user_accounts_screen = UserAccounts(session, master=self)
        self.withdraw_confirm_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_withdraw(self):
        # Switch to home screen from withdraw confirmation screen
        self.withdraw_confirm_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 

    def switch_to_transfer_confirm_screen(self, session):
        # Switch to transfer screen
        self.transfer_confirm_screen = ConfirmTransferScreen(session, master = self)
        self.transfer_screen.pack_forget()
        self.transfer_confirm_screen.pack()
    
    def switch_to_user_accounts_from_transfer_screen(self, session):
        # Switch to user accounts screen from transfer confirmation screen
        self.user_accounts_screen = UserAccounts(session, master=self)
        self.transfer_confirm_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_transfer(self):
        # Switch to home screen from transfer confirmation screen
        self.transfer_confirm_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 

    def switch_to_check_balance_screen(self, session):
        self.check_balance_screen = CheckBalance(session, master=self)
        self.transactions_screen.pack_forget()
        self.check_balance_screen.pack()

    def switch_to_user_accounts_from_check_balance_screen(self, session):
        # Switch to user accounts screen from transfer confirmation screen
        self.user_accounts_screen = UserAccounts(session, master=self)
        self.check_balance_screen.pack_forget()
        self.user_accounts_screen.pack()

    def switch_to_home_screen_from_check_balance(self):
        # Switch to home screen from transfer confirmation screen
        self.check_balance_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack() 

    def switch_to_home_view(self):
        self.account_creation_screen.pack_forget()
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack()


app = MainApp()
app.mainloop()