from peewee import *
import sqlite3

conn = sqlite3.connect('atm.db')

c = conn.cursor()

# Insert the data

# Joshua Kim - Person, Checking, Saving
# Ethan Bautista - ATM, Transactions, Account 

# c.execute("""CREATE TABLE PERSON    (
#             personID INT(5) PRIMARY KEY,
#             firstName VARCHAR(50),
#             lastName VARCHAR(50),
#             emailAddress VARCHAR(50),
#             telephoneNumber VARCHAR(12),
#             physicalAddress VARCHAR(50)
#             )""")

# c.execute("INSERT INTO PERSON VALUES (23099, 'John', 'Doe', 'jdoe@gmail.com', '123-456-7890', '101 Crestview Drive, Pomona, 91023')")
# c.execute("INSERT INTO PERSON VALUES (45826, 'Will', 'Smith', 'wsmith@gmail.com', '234-567-8910', '630 Victoria Avenue, Salinas, 91432')")
# c.execute("INSERT INTO PERSON VALUES (97502, 'Jack', 'Sparrow', 'jsparrow@gmail.com', '345-678-9101', 'Eagleview Drive, Chino, 93240')")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute("""CREATE TABLE CHECKING  (
#             checkingID INT(5) PRIMARY KEY,
#             accountNum INT(5),
#             accountBalance INT(10),
#             FOREIGN KEY(accountNum) REFERENCES Account(accountNum)
#             )""")

# c.execute("INSERT INTO CHECKING VALUES (31928, 47839, 5231)")
# c.execute("INSERT INTO CHECKING VALUES (39281, 74803, 6132)")
# c.execute("INSERT INTO CHECKING VALUES (59483, 19304, 4102)")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute("""CREATE TABLE SAVING (
#             savingID INT(5) PRIMARY KEY,
#             accountNum INT(5),
#             accountBalance INT(10),
#             FOREIGN KEY(accountNum) REFERENCES Account(accountNum)
#             )""")

# c.execute("INSERT INTO SAVING VALUES (19283, 47839, 20236)")
# c.execute("INSERT INTO SAVING VALUES (37566, 74803, 15131)")
# c.execute("INSERT INTO SAVING VALUES (99998, 19304, 10103)")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute("""CREATE TABLE ACCOUNT (
#             accountNum INT(5) PRIMARY KEY,
#             personID INT(5),
#             pinNum INT(4),
#             FOREIGN KEY(personID) REFERENCES Person(personID)
# )""")

# c.execute("INSERT INTO ACCOUNT VALUES (47839, 23099, 1111)")
# c.execute("INSERT INTO ACCOUNT VALUES (74803, 45826, 1234)")
# c.execute("INSERT INTO ACCOUNT VALUES (19304, 97502, 4321)")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute("""
# CREATE TABLE ATM (
#   atmID INT(5) PRIMARY KEY,
#   location VARCHAR(50) NOT NULL,
#   cashAvailable INT(6) NOT NULL,
#   PRIMARY KEY (atmID)
# );
# """)

# c.execute("INSERT INTO ATM (atmID, location, cashAvailable) VALUES (00001, 'BRIC', 100000))
# c.execute("INSERT INTO ATM (atmID, location, cashAvailable) VALUES (00002, 'PonyExpress', 100000))
# c.execute("INSERT INTO ATM (atmID, location, cashAvailable) VALUES (00003, 'Library', 100000))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute('''
# CREATE TABLE "Transactions" (
#   transactionID INT(5) PRIMARY KEY,
#   accountNum INT(5),
#   type VARCHAR(20) NOT NULL,
#   date DATE NOT NULL,
#   amount(6) INT NOT NULL,
#   FOREIGN KEY (accountNum) REFERENCES Account(accountNum)
# );
# ''')

# # Insert the data with double quotes around the table name
# c.execute('''
# INSERT INTO "Transaction" (transactionID, accountNum, type, date, amount) 
# VALUES (?, ?, ?, ?, ?)
# ''', (11111, 47839, 'Savings', '2023-04-11', 20))
# c.execute('''
# INSERT INTO "Transaction" (transactionID, accountNum, type, date, amount) 
# VALUES (?, ?, ?, ?, ?)
# ''', (11112, 74803, 'Checkings', '2023-03-25', 100))
# c.execute('''
# INSERT INTO "Transaction" (transactionID, accountNum, type, date, amount) 
# VALUES (?, ?, ?, ?, ?)
# ''', (11113, 19304, 'Savings', '2023-04-04', 75))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# c.execute("SELECT * FROM Transactions")
# print(c.fetchall())

conn.commit()
conn.close()

