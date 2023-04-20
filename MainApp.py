import tkinter as tk

class HomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create Welcome message label
        self.welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Create Username label and input box
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        # Create Password label and input box
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Create Sign-in button
        self.signin_button = tk.Button(self, text="Sign-in", command=self.signin_clicked)
        self.signin_button.pack(pady=10)

        # Create "Don't have an account?" message
        self.create_account_message = tk.Label(self, text="Don't have an account?")
        self.create_account_message.pack(pady=5)

        # Create Create account button
        self.create_account_button = tk.Button(self, text="Create account", command=self.create_account_clicked)
        self.create_account_button.pack(pady=5)

    def signin_clicked(self):
        #Switch to user accounts screen
        self.master.switch_to_user_accounts_screen()

    def create_account_clicked(self):
        # Switch to account creation screen
        self.master.switch_to_account_creation_screen()



class UserAccounts(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
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
        self.savings_account_button = tk.Button(self, text="College\nSavings\nAccount", command=self.college_checking_clicked)
        self.savings_account_button.pack(pady=10)

        # Create Personal Spending Account button
        self.spending_account_button = tk.Button(self, text="Personal\nSpending\nAccount", command=self.college_checking_clicked)
        self.spending_account_button.pack(pady=10)

    def college_checking_clicked(self):
        # Switch to transactions screen
        self.master.switch_to_transactions_screen()


class Transactions(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="What would you like\nto do today?", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=10)

        # Create Check balance button
        self.check_balance_button = tk.Button(self, text="Check\nBalance", command=self.withdraw_clicked)
        self.check_balance_button.pack(pady=5)

        # Create Deposit button
        self.deposit_button = tk.Button(self, text="Deposit", command=self.withdraw_clicked)
        self.deposit_button.pack(pady=5)

        # Create Withdraw button
        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw_clicked)
        self.withdraw_button.pack(pady=5)

        # Create Transfer button
        self.transfer_button = tk.Button(self, text="Transfer", command=self.withdraw_clicked)
        self.transfer_button.pack(pady=5)

    
    def withdraw_clicked(self):
        # Switch to withdraw screen
        self.master.switch_to_withdraw_screen() 


class WithdrawScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome labels 
        self.welcome_label = tk.Label(self, text="Please enter the amount\nto withdraw", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=20)

        # Create Amount label
        self.amount_label = tk.Label(self, text="Amount: $")
        self.amount_label.pack(side="left")

        # Create Amount entry
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="left")

        # Create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.withdraw_submit_clicked)
        self.submit_button.pack(pady=5)

    def withdraw_submit_clicked(self):
        # Switch to withdraw confirm screen
        self.master.switch_to_withdraw_confirm_screen()

class WithdrawConfirmScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="Please take the money\nfrom the withdraw port", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=20)

        #Create question label
        self.question_label = tk.Label(self, text="Is there anything else\n you want to do today?",  font=("Arial", 16))
        self.question_label.pack(pady=20)

        # Create Yes button
        self.yes_button = tk.Button(self, text="Yes", command=self.yes_clicked)
        self.yes_button.pack(side="left", padx=20)

        # Create No button
        self.no_button = tk.Button(self, text="No", command=self.no_clicked)
        self.no_button.pack(side="right", padx=20)

    def yes_clicked(self):
        # Placeholder method
        print("YES")

    def no_clicked(self):
        # Placeholder method
        print("NO")



class AccountCreationScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create account creation labels 
        self.account_creation_label = tk.Label(self, text="Create account:")
        self.account_creation_label.pack(pady=10)

        # Create username label and input box
        self.username_label = tk.Label(self, text="Name:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Create phone number label and input box
        self.phone_num_label = tk.Label(self, text="Phone number:")
        self.phone_num_label.pack()
        self.phone_num_entry = tk.Entry(self)
        self.phone_num_entry.pack()

        # Create email label and input box
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        # Create date of birth label and input box
        self.dob_label = tk.Label(self, text="Date of birth:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack()

        # Create submit label and button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_clicked)
        self.submit_button.pack(pady=5)

    def submit_clicked(self):
        # Switch to password creation screen
        self.master.switch_to_password_creation_screen()


class PasswordCreationScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="Please set your password.", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Create password label and input box
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

        # Create confirm-password label and input box
        self.confirm_password_label = tk.Label(self, text="Re-confirm password:")
        self.confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(self)
        self.confirm_password_entry.pack()

       
        # Create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_clicked)
        self.submit_button.pack(pady=5)

    def submit_clicked(self):
        # Switch to confirmation screen
        self.master.switch_to_confirmation_screen()



class ConfirmCreationScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="Congratulations! Your account\nis all set up!", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Create actions labbel
        self.actions_label = tk.Label(self, text="Would you like to perform any\nactions with your account?:")
        self.actions_label.pack()

        # Create yes label and button
        self.yes_button = tk.Button(self, text="Yes", command=self.yes_clicked)
        self.yes_button.pack(side="left", padx=20)

        # Create no label and button
        self.no_button = tk.Button(self, text="No", command=self.no_clicked)
        self.no_button.pack(side="right", padx=20)

    def yes_clicked(self):
        # Placeholder method
        print("YES")

    def no_clicked(self):
        # Placeholder method
        print("NO")




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