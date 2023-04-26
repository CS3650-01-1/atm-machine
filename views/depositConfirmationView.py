import tkinter as tk
class DepositCreationScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create welcome label
        self.welcome_label = tk.Label(self, text="Money sucessfully deposited\ninto account.", font=("Arial", 24))
        self.welcome_label.pack(side="top", pady=10)

        # Create actions labbel
        self.actions_label = tk.Label(self, text="Would you like to perform any\nactions with your account?")
        self.actions_label.pack()

        # Create yes label and button
        self.yes_button = tk.Button(self, text="Yes", command=self.yes_clicked)
        self.yes_button.pack(side="left", padx=20)

        # Create no label and button
        self.no_button = tk.Button(self, text="No", command=self.no_clicked)
        self.no_button.pack(side="right", padx=20)

    def yes_clicked(self):
       # Switch to accounts screen
       self.master.switch_to_user_accounts_from_deposit_screen()  

    def no_clicked(self):
        # Switch to home screen
        self.master.switch_to_home_screen_from_deposit()