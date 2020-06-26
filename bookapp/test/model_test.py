from .context import bookapp
import pytest
from bookapp import app, db
from bookapp.models import Book 


def test_config_db():
    assert app.config['SQLALCHEMY_DATABASE_URI'] != ''

def test_add_books():
    book_3 = Book(title="Beasts & Barbarians",
                description="Swords and sandals fantasy setting for Savage Worlds",
                isbn='test-9999')
    db.session.add(book_3)
    assert Book.query.filter_by(isbn='test-9999').first().title == "Beasts & Barbarians"

