from datetime import datetime

'''
class representing the log of a transaction
'''
class Transaction:
    def __init__(self, type, amount, transaction_id, account):
        self.type = type
        self.date = datetime.now    # log datetime on init
        self.amount = amount
        self.transaction_id = transaction_id
        self.account = account

    def save(self):
        print("Saved Transaction:\n%s" % self)
        #TODO: logic for recording into database eventually

    def __str__(self):  # something to print for future debugging
        # buncha objects so cant print until other str methods are done
        return f"Type: {self.type}\nDate: {self.date}\nAmount: {self.amount}\nTransaction ID: {self.transaction_id}\nAccount ID: {self.account.accountNum}"