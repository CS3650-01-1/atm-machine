from models.atm import ATM

class viewTransactionsController:
    def __init__(self, view, session):
        self.view = view
        self.session = session
    
    def get_all_transactions(self):
        if self.session.accountType == "checking":
            return ATM.get_all_transactions(self.session.checkingID)
        elif self.session.accountType == "savings":
            return ATM.get_all_transactions(self.session.savingsID)