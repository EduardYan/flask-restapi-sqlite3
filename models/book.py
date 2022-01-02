"""
This module have the model
for the book in the database.
"""

from utils.db import db

class Books(db.Model):
    """
    This is a class for create a data model
    for save in the database.
    """

    # columns for the table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)

    def __init__(self, name:str, price:str) -> None:
        # the id not is required
        self.name = name
        self.price = price
