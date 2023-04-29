class Session:
    def __init__(self):
        self.accountID = None
        self.savingsID = None
        self.checkingID = None

    def __str__(self):
        return f"Account ID: {self.accountID}\nSavings ID: {self.savingsID}\nChecking ID: {self.checkingID}"