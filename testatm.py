from models import atm

bric = atm.ATM.retrieve(1)

bric.deposit_cash(100, 19283, "savings")