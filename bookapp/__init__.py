from flask import Flask

app = Flask(__name__)

from bookapp import routes
