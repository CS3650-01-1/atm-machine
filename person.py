'''
class representing a person; acts as a "master" account to multiple bank accounts
'''

class Person:
    def __init__(self, first_name, last_name, email_address, telephone_number, physical_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.telephone_number = telephone_number
        self.physical_address = physical_address

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nEmail: {self.email_address}\nPhone: {self.telephone_number}\nAddress: {self.physical_address}"