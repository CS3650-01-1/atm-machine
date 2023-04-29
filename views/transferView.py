import tkinter as tk

from controllers import transferBalanceController


class TransferScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.welcome_label = tk.Label(self, text="Enter amount to transfer:", font=("Arial", 18))
        self.welcome_label.pack(side="top", pady=10)

        # Create an entry for the amount input
        amount_entry = tk.Entry(self)
        amount_entry.pack(pady = 10)

        self.accounts_label = tk.Label(self, text="Pick account to transfer to:", font=("Arial", 14))
        self.accounts_label.pack(side="top", pady=5)

        # Create a frame for the radio buttons
        account_frame = tk.Frame(self)
        account_frame.pack(pady=10)

        # Create radio buttons for the bank accounts
        account_var = tk.StringVar()
        account_var.set("Savings Account")

        if(account_type == checking):
            account_savings_rb = tk.Radiobutton(account_frame, text="Savings Account", variable=account_var, value="Savings Account")
            account_savings_rb.pack(side="left")
        else:
            account_checking_rb = tk.Radiobutton(account_frame, text="Checking Account", variable=account_var, value="Checking Account")
            account_checking_rb.pack(side="left")




        # Create a submit button
        submit_button = tk.Button(self, text="Submit", command=self.transfer_submit_clicked)
        submit_button.pack(pady=10)

    def transfer_submit_clicked(self):
        transferBalanceController.transfer_balance(self.amount_entry.get(), account, destination)
        self.master.switch_to_transfer_confirm_screen()

