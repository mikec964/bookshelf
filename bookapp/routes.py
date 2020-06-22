from flask import Flask, render_template
from bookapp import app

# app = Flask(__name__) # must be in __init__.py

@app.route('/')
def hello_world():
    return render_template('home.html', title="Home Page", greeting='Bienvenido')


# if __name__ == '__main__':
#     app.debug = True
#     app.run()
