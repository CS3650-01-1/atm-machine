import tkinter as tk
class UserAccounts(tk.Frame):
    def __init__(self, session, master=None):
        super().__init__(master)
        self.session = session
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create Welcome message label
        self.welcome_label = tk.Label(self, text="Please choose which\naccount you would like to\ncomplete the transaction on", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=10)

        # Create College Checkings Account button
        self.checkings_account_button = tk.Button(self, text="College\nChecking\nAccount", command=self.college_checking_clicked)
        self.checkings_account_button.pack(pady=10)

        # Create College Savings Account button
        self.savings_account_button = tk.Button(self, text="College\nSavings\nAccount", command=self.college_savings_clicked)
        self.savings_account_button.pack(pady=10)

        # Create log out button
        self.log_out_button = tk.Button(self, text="Log Out", command=self.log_out_button_clicked)
        self.log_out_button.pack(pady=10)

    def college_checking_clicked(self):
        # Switch to transactions screen
        self.session.accountType = "checking"
        self.master.switch_to_transactions_screen(self.session)

    def college_savings_clicked(self):
        self.session.accountType = "savings"
        self.master.switch_to_transactions_screen(self.session)

    def log_out_button_clicked(self):
        self.master.switch_to_home_view(self)