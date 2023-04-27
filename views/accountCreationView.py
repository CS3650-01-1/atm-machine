import tkinter as tk
from controllers import accountCreationController

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
        self.full_name_label = tk.Label(self, text="Full Name:")
        self.full_name_label.pack()
        self.full_name_entry = tk.Entry(self)
        self.full_name_entry.pack()

        # Create name label and input box
        self.username_label = tk.Label(self, text="Username:")
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

        # Create physical address label and input box
        self.dob_label = tk.Label(self, text="Address:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack()

        # Create submit label and button
        self.submit_button = tk.Button(self, text="Submit", command=lambda:[self.submit_clicked(), accountCreationController.submit_account()])
        self.submit_button.pack(pady=5)

    def submit_clicked(self):
        # Switch to password creation screen
        self.master.switch_to_password_creation_screen()
