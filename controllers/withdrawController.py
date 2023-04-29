import sqlite3

from models import atm
from views.depositView import *
from models.accountModel import *
from models.checkingsModel import *
from models.savingsModel import *
DATABASE = "atm.db"

def submit_withdraw(amount):
    atm.withdraw_cash(amount)