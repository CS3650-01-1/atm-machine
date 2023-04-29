import sqlite3

from models import atm
from models.atm import *
DATABASE = "atmdb"

def transfer_balance(amount, origin, destination):
    atm.transfer_balance(amount, origin, destination)
