from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bookapp import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text())
    isbn = db.Column(db.String(13))

    def __repr__(self):
        return f"Book('{self.title}', '{self.isbn}')"
