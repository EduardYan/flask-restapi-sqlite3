"""
This is the principal file
for execute the server.

The server is in port 3000.

"""

from flask import Flask
from routes.books import books
from config import DB_PATH
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# deffiniting where is the database
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

# showing blue print
app.register_blueprint(books)
