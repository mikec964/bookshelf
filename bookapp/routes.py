from flask import Flask, render_template, url_for, redirect
from bookapp.models import Book 
from bookapp import app, db
from bookapp.forms import PostBook


@app.route('/')
def hello_world():
    books = Book.query.all()
    return render_template('home.html', title= "Home Page", 
        greeting='Bienvenido', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    '''Create new book'''
    form = PostBook()
    if form.validate_on_submit():
        book = Book(title=form.title.data, description=form.description.data, isbn=form.isbn.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('hello_world'))
    return render_template('add_book.html', title= "Add Book", 
        legend="New Book", form=form)


@app.route('/book/<int:book_id>')
def show_book(book_id):
    '''Read book description'''
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', title=book.title,
        book=book)


@app.route('/test')
def test_out():
    book = Book.query.first()
    return render_template('book.html', title=book.title,
        book=book)

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
