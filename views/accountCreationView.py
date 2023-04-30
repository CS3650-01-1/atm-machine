import tkinter as tk
from controllers.accountCreationController import AccountCreationController

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
        
        # Create password and input box
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()

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
        self.physical_address_label = tk.Label(self, text="Address:")
        self.physical_address_label.pack()
        self.physical_address_entry = tk.Entry(self)
        self.physical_address_entry.pack()

        # create error labels
        self.username_taken_error_label = tk.Label(self, text="Username is taken!")
        self.invalid_field_inputs_error_label = tk.Label(self, text="One or more fields have invalid content!")
        self.error_labels = []
        self.error_labels.append(self.username_taken_error_label)
        self.error_labels.append(self.invalid_field_inputs_error_label)

        # Create submit label and button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_clicked)
        self.submit_button.pack(pady=5)

        # create back button
        self.back_button = tk.Button(self, text="Back", command=self.back_button_clicked)
        self.back_button.pack(pady=5)

    def submit_clicked(self):
        # Switch to password creation screen
        controller = AccountCreationController(self)
        controller.submit_account(self.full_name_entry.get(),self.username_entry.get(), self.password_entry.get(), self.email_entry.get(), self.phone_num_entry.get(), self.physical_address_entry.get())
    
    def hide_error_labels(self):
        for label in self.error_labels:
            label.pack_forget()
        
    def back_button_clicked(self):
        self.master.switch_to_home_view(self)
