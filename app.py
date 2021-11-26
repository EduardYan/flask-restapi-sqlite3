"""
This is the principal file
for execute the server.

The server is in port 6000.

"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from connections import db

app = Flask(__name__)
# deffiniting where is the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db

db = SQLAlchemy(app)


class Book(db.Model):
    """
    This is a class for create a data model
    for save in the database.
    """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)


@app.route('/')
@app.route('/books')
def getBooks():
    """
    This route is for get
    the books of the database.

    Return the list of books, in the database.

    """
    books = Book.query.all()

    books_list = [{'id': b.id, 'name': b.name, 'price': b.price} for b in books]

    return jsonify({
        "message": "Books's list",
        "books": books_list
    })


@app.route('/books/<string:id>')
def getBook(id):
    """
    This route is for get a book for your name.

    Recive the book name por parameter.

    """

    bookFound = Book.query.filter_by(id = int(id)).first()

    if (bookFound == None):
        return jsonify({"message": "Product not Found"})

    book = {'id': bookFound.id, 'name': bookFound.name, 'price': bookFound.price}

    return jsonify({
        "message": "Book Found",
        "book": book
    })


@app.route('/', methods=['POST'])
@app.route('/books', methods=['POST'])
def addBook():
    """
    This is the route for add
    a new book at the database.

    """
    # controlling the execpt in case not are json data, if not form data
    try:
        book = Book(name = request.json['name'], price = float(request.json['price']))

    except TypeError:
        # getting the book data, from request.form
        book = Book(name = request.form['name'], price = float(request.form['price']))

        # adding the book in the database
        db.session.add(book)

        # consulting again all values
        newBooks = Book.query.all()

        db.session.commit()

        books = [{'id': b.id, 'name': b.name, 'price': b.price} for b in newBooks]

        return jsonify({
            "message": "Product Added Sucessfully",
            "newBook": {'id': book.id, 'name': book.name, 'price': book.price},
            "newBooks": books

        })

    else:
        # adding the book in the database
        db.session.add(book)

        # consulting again all values
        newBooks = Book.query.all()

        db.session.commit()

        books = [{'id': b.id, 'name': b.name, 'price': b.price} for b in newBooks]

        return jsonify({
            "message": "Product Added Sucessfully",
            "newBook": {'id': book.id, 'name': book.name, 'price': book.price},
            "newBooks": books

        })


@app.route('/books/<string:id>', methods=['DELETE'])
def deleteBook(id):
    """
    This is the route for delete
    a book of the database.

    Recive the id of the book for delete.

    """

    # validating if the book not in the database
    if (Book.query.filter_by(id = int(id)).first() == None):
        return jsonify({"message": "Book not Found"})

    # deleting the book
    Book.query.filter_by(id = int(id)).delete()

    books_news = Book.query.all()
    new_books_list = [{'id': b.id, 'name': b.name, 'price': b.price} for b in books_news]

    db.session.commit()


    return jsonify({
        "message": f"Book with id {id} Deleted Sucessfully",
        "newBookList": new_books_list
        })


@app.route('/books/<string:id>', methods=['PUT'])
def updateBook(id):
    """
    This is the route for update
    a book of the database.

    Recive the id of the book for update.

    """
    # getting the book for update
    book = Book.query.filter_by(id = int(id)).first()

    # validating if the book is in the database
    if not book == None:
        # getting the book old
        book_old = {'id': book.id, 'name': book.name, 'price': book.price}

        # changing the values in the database
        book.name = request.form['name']
        book.price = request.form['price']

        db.session.commit()

        return jsonify({
            "message": "Product Update Sucessfully",
            "productOld": book_old,
            "productUpdated": {'id': book.id, 'name': book.name, 'price': book.price}
        })

    return jsonify({"message": "Product not Found"})


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
