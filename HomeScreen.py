import tkinter as tk

class HomeScreen:
    def __init__(self, master):
        self.master = master
        master.title("ATM System")


        self.button1 = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.button1.pack()

        self.button2 = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.button2.pack()

        self.button3 = tk.Button(master, text="Deposit", command=self.deposit)
        self.button3.pack()

        self.button4 = tk.Button(master, text="Transfer", command=self.transfer)
        self.button4.pack()

        self.button6 = tk.Button(master, text="Exit", command=master.quit)
        self.button6.pack()

    def check_balance(self):
        self.check_balance_screen = tk.Toplevel(self.master)
        self.check_balance_screen.title("Check Balance")

    def withdraw(self):
        self.withdraw_screen = tk.Toplevel(self.master)
        self.withdraw_screen.title("Withdraw")

    def deposit(self):
        self.deposit_screen = tk.Toplevel(self.master)
        self.deposit_screen.title("Deposit")

    def transfer(self):
        self.transfer_screen = tk.Toplevel(self.master)
        self.transfer_screen.title("Transfer")



root = tk.Tk()
gui = HomeScreen(root)
root.mainloop()