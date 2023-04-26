import tkinter as tk

from main import MainApp


class DepositScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
    #Create Deposit Label
        self.depLabel = tk.Label(text = "Please Specify the Amount \nYou Are Depositing", font = ("Arial", 20))
        self.depLabel.pack(side="top", pady=20)

        # create deposit amount label
        self.amtLabel = tk.Label(self, text = "$ ")
        self.amtLabel.pack(side = "left")

        #craete deposit amount entry
        self.depAmount = tk.Entry(self)
        self.depAmount.pack(side="left")

        #Create a submit button after user inputs amount of deposit
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_deposit())
        self.submit_button.pack(pady=5)

    def submit_deposit(self):
        #Go back to home screen
        self.master.switch_to_withdraw_confirm_screen()




