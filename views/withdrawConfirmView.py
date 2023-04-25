import tkinter as tk
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
        # Switch to accounts screen
        self.master.switch_to_user_accounts_from_withdraw_screen()

    def no_clicked(self):
        # Switch to home screen
        self.master.switch_to_home_screen_from_withdraw()
