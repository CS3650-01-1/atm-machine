from models import atm

bric = atm.ATM.retrieve(1)

bric.deposit_cash(200, 19283, "savings")