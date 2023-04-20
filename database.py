from peewee import *
import sqlite3

conn = sqlite3.connect('atm.db')


c = conn.cursor()



# Insert the data
# c.execute("INSERT INTO Transactions (transactionID, accountNum, type, date, amount) VALUES (?, ?, ?, ?, ?)", (11111, 47839, 'Savings', '2023-04-11', 20))
# c.execute("INSERT INTO Transactions (transactionID, accountNum, type, date, amount) VALUES (?, ?, ?, ?, ?)", (11112, 74803, 'Checkings', '2023-03-25', 100))
# c.execute("INSERT INTO Transactions (transactionID, accountNum, type, date, amount) VALUES (?, ?, ?, ?, ?)", (11113, 19304, 'Savings', '2023-04-04', 75))

c.execute("SELECT * FROM Transactions")
print(c.fetchall())

conn.commit()
conn.close()

