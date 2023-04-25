import tkinter as tk
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