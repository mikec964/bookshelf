from flask import Flask, render_template, url_for, redirect, request
from bookapp.models import Book 
from bookapp import app, db
from bookapp.forms import PostBook


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', title= "Home Page", 
        greeting='Bienvenido', books=books)


@app.route('/add', methods=['GET', 'POST'])
def create_book():
    '''Create new book'''
    form = PostBook()
    if form.validate_on_submit():
        book = Book(title=form.title.data, description=form.description.data, isbn=form.isbn.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_book.html', title= "Add Book", 
        legend="New Book", form=form)


@app.route('/book/<int:book_id>')
def show_book(book_id):
    '''Read book description'''
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', title=book.title,
        book=book)


@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    '''Update book'''
    book = Book.query.get_or_404(book_id)
    form = PostBook()
    if form.validate_on_submit():
        book.title = form.title.data
        book.description = form.description.data
        book.isbn = form.isbn.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = book.title
        form.description.data = book.description
        form.isbn.data = book.isbn
    return render_template('create_book.html', title= "Update Book", 
        legend="Book", form=form)


@app.route('/test')
def test_out():
    book = Book.query.first()
    return render_template('book.html', title=book.title,
        book=book)

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
