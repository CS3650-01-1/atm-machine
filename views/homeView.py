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
        self.create_account_button = tk.Button(self, text="Create account", command=lambda: [self.create_account_clicked(), sign_In()])
        self.create_account_button.pack(pady=5)

    def signin_clicked(self):
        #Switch to user accounts screen
        self.master.switch_to_user_accounts_screen()

    def create_account_clicked(self):
        # Switch to account creation screen
        self.master.switch_to_account_creation_screen()
