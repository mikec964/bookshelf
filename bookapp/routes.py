from flask import Flask, render_template
from bookapp.models import Book 
from bookapp import app

@app.route('/')
def hello_world():
    return render_template('home.html', title= "Home Page", greeting='Bienvenido')

@app.route('/test')
def test_out():
    my_book = Book.query.first()
    return render_template('home.html', title= my_book.title,
        greeting='Out=' + my_book.isbn)

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
