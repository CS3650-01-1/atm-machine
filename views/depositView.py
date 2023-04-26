import tkinter as tk

class DepositScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create deposit screen label and prompt the user for the amount to deposit
        self.welcome_label = tk.Label(self, text="Please specify the amount\nyou are depositing", font=("Arial", 20))
        self.welcome_label.pack(side="top", pady=10)

        # Create Amount label
        self.amount_label = tk.Label(self, text="Amount to deposit:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # Create button to submit deposit and go back to the main menu
        self.submit_button = tk.Button(self, text="Deposit", command=self.submit_deposit)
        self.submit_button.pack(pady=10)


    def submit_deposit(self):
        #Go back to home screen
        self.master.switch_to_deposit_confirmation_screen()




