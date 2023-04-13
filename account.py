'''
class representing a bank account; its transaction log is done through database relation
'''

class Account:
    def __init__(self, accountNum, balance, card_number, pin):
        self.accountNum = accountNum 
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    def __str__(self):
        return f"Account ID: {self.accountNum}\nBalance: {self.balance}"