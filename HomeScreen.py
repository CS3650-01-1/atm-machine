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
        #Logic to be implemented later
        print("Sign-in clicked")

    def create_account_clicked(self):
        # Switch to account creation screen
        self.master.switch_to_account_creation_screen()

class AccountCreationScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create account creation labels and input boxes
        self.account_creation_label = tk.Label(self, text="Create account:")
        self.account_creation_label.pack(pady=10)


        self.username_label = tk.Label(self, text="Name:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.phone_num_label = tk.Label(self, text="Phone number:")
        self.phone_num_label.pack()
        self.phone_num_entry = tk.Entry(self)
        self.phone_num_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.dob_label = tk.Label(self, text="Date of birth:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack()

        #Need to include password page

    def create_account(self):
        #Logic to be implemented later
        print("Account created")

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM System")
        self.geometry("800x300")
        self.home_screen = HomeScreen(self)
        self.account_creation_screen = AccountCreationScreen(self)
        self.home_screen.pack()

    def switch_to_account_creation_screen(self):
        self.home_screen.pack_forget()
        self.account_creation_screen.pack()

app = MainApp()
app.mainloop()