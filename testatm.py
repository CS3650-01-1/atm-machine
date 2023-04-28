from models import atm

bric = atm.ATM.retrieve(1)

bric.deposit_cash(1, 19283, 47839, "savings")