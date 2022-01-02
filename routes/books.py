"""
This file have the routes for the books in
the server
"""

from flask import Blueprint, jsonify, request
from models.book import Books
from utils.db import db

books = Blueprint('books', __name__)

@books.route('/')
@books.route('/books')
def getBooks():
    """
    This route is for get
    the books of the database.

    Return the list of books, in the database.

    """
    books = Books.query.all()

    books_list = [{'id': b.id, 'name': b.name, 'price': b.price} for b in books]

    return jsonify({
        "message": "Books's list",
        "books": books_list
    })


@books.route('/books/<string:id>')
def getBook(id):
    """
    This route is for get a book for your name.

    Recive the book name por parameter.

    """

    bookFound = Books.query.filter_by(id = int(id)).first()

    if (bookFound == None):
        return jsonify({"message": "Product not Found"})

    book = {'id': bookFound.id, 'name': bookFound.name, 'price': bookFound.price}

    return jsonify({
        "message": "Book Found",
        "book": book
    })


@books.route('/', methods=['POST'])
@books.route('/books', methods=['POST'])
def addBook():
    """
    This is the route for add
    a new book at the database.

    Data for recived:
    name
    price

    """
    # controlling the execpt in case not are json data, if not form data
    try:
        book = Books(name = request.json['name'], price = float(request.json['price']))

    except TypeError:
        # getting the book data, from request.form
        book = Books(name = request.form['name'], price = float(request.form['price']))

        # adding the book in the database
        db.session.add(book)

        # consulting again all values
        newBooks = Books.query.all()

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
        newBooks = Books.query.all()

        db.session.commit()

        books = [{'id': b.id, 'name': b.name, 'price': b.price} for b in newBooks]

        return jsonify({
            "message": "Product Added Sucessfully",
            "newBook": {'id': book.id, 'name': book.name, 'price': book.price},
            "newBooks": books

        })


@books.route('/books/<string:id>', methods=['DELETE'])
def deleteBook(id):
    """
    This is the route for delete
    a book of the database.

    Recive the id of the book for delete.

    """

    # validating if the book not in the database
    if (Books.query.filter_by(id = int(id)).first() == None):
        return jsonify({"message": "Book not Found"})

    # deleting the book
    Books.query.filter_by(id = int(id)).delete()

    books_news = Books.query.all()
    new_books_list = [{'id': b.id, 'name': b.name, 'price': b.price} for b in books_news]

    db.session.commit()


    return jsonify({
        "message": f"Book with id {id} Deleted Sucessfully",
        "newBookList": new_books_list
        })


@books.route('/books/<string:id>', methods=['PUT'])
def updateBook(id):
    """
    This is the route for update
    a book of the database.

    Recive the id of the book for update.

    """
    # getting the book for update
    book = Books.query.filter_by(id = int(id)).first()

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
