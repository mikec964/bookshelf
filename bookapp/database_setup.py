from bookapp.models import db, Book 

db.create_all()

book_1 = Book(id=1, title="50 Fathoms Explorer's Edition",
            description="Pirate fantasy setting for Savage Worlds Deluxe Edition",
            isbn='978-1-937013-18-9')
db.session.add(book_1)

book_2 = Book(id=2, title="Savage Worlds Deluxe Edition",
            description="Fast, Furious, Fun and universal RPG rules",
            isbn='')
db.session.add(book_2)

book_3 = Book(title="Beasts & Barbarians",
            description="Swords and sandals fantasy setting for Savage Worlds",
            isbn='')
db.session.add(book_3)

db.session.commit()

print(Book.query.all())
print(Book.query.first())
