from .context import bookapp
import pytest

from bookapp import app, db
from bookapp.models import Book 


def test_config_db():
    assert app.config['SQLALCHEMY_DATABASE_URI'] != ''

def test_add_books():
    db.drop_all()
    db.create_all()
    book_2 = Book(title="Gold and Glory",
                description="Old school random dungeons and adventurers",
                isbn='test-1111')
    db.session.add(book_2)
    book_3 = Book(title="Beasts and Barbarians",
                description="Swords and sandals fantasy setting",
                isbn='test-2222')
    db.session.add(book_3)
    db.session.commit()
    assert Book.query.filter_by(isbn='test-2222').first().title == "Beasts and Barbarians"
    assert len(Book.query.all()) == 2
