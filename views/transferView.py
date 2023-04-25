import tkinter as tk

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
        account_var.set("Account 1")

        account_1_rb = tk.Radiobutton(account_frame, text="Account 1", variable=account_var, value="Account 1")
        account_2_rb = tk.Radiobutton(account_frame, text="Account 2", variable=account_var, value="Account 2")
        account_3_rb = tk.Radiobutton(account_frame, text="Account 3", variable=account_var, value="Account 3")

        account_1_rb.pack(side="left")
        account_2_rb.pack(side="left")
        account_3_rb.pack(side="left")

        # Create a submit button
        submit_button = tk.Button(self, text="Submit", command=self.transfer_submit_clicked)
        submit_button.pack(pady=10)

    def transfer_submit_clicked(self):
        self.master.switch_to_transfer_confirm_screen()

