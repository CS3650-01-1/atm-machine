import tkinter as tk
class Transactions(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.master = master
        self.session = session
        self.create_widgets()
        print(self.session)

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="What would you like\nto do today?", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=10)

        # Create Check balance button
        self.check_balance_button = tk.Button(self, text="Check\nBalance", command=self.check_balance_clicked)
        self.check_balance_button.pack(pady=5)

        # Create Deposit button
        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit_clicked)
        self.deposit_button.pack(pady=5)

        # Create Withdraw button
        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw_clicked)
        self.withdraw_button.pack(pady=5)

        # Create Transfer button
        self.transfer_button = tk.Button(self, text="Transfer", command=self.transfer_clicked)
        self.transfer_button.pack(pady=5)

        # Create View Transactions button
        self.view_trans_button = tk.Button(self, text="View Transactions", command=self.view_trans_clicked)
        self.view_trans_button.pack(pady=5)

        # Create Switch Accounts button
        self.switch_account_button = tk.Button(self, text="Switch Account", command=self.switch_account_button_clicked)
        self.switch_account_button.pack(pady=10)

        # Create log out button
        self.log_out_button = tk.Button(self, text="Log Out", command=self.log_out_button_clicked)
        self.log_out_button.pack(pady=10)

    def check_balance_clicked(self):
        # Switch to check balance screen
        self.master.switch_to_check_balance_screen(self.session)

    def deposit_clicked(self):
        self.master.switch_to_deposit_screen(self.session)

    def withdraw_clicked(self):
        # Switch to withdraw screen
        self.master.switch_to_withdraw_screen(self.session) 

    def transfer_clicked(self):
        # Switch to transfer screen
        self.master.switch_to_transfer_screen(self.session)     

    def view_trans_clicked(self):
        self.master.switch_to_view_trans_screen(self.session)

    def log_out_button_clicked(self):
        self.master.switch_to_home_view(self)

    def switch_account_button_clicked(self):
        self.master.switch_to_user_accounts_view(self, self.session)