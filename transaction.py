'''
class representing the log of a transaction
'''
class Transaction:
    def __init__(self, type, date, amount, transaction_id, account, authentication) -> None:
        self.type = type
        self.date = date
        self.amount = amount
        self.transaction_id = transaction_id
        self.account = account
        self.authentication = authentication