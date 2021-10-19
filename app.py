"""
This is the principal file
for execute the server.

The server is in port 6000.

"""

from flask import Flask, jsonify, request
from sqlite3 import connect
from connections import getCursor, db

app = Flask(__name__)


@app.route('/books')
def getBooks():
    """
    This route is for get
    the books of the database.

    Return the list of books, in the database.

    """
    con = connect(db)
    cursor = getCursor(con)
    cursor.execute("SELECT * FROM books")

    # getting the books in tuples of the databas
    books = cursor.fetchall()

    con.commit()
    cursor.close()

    # list of books for return
    books_list = [{'id': book[0], 'name': book[1], 'price': book[2]} for book in books]

    if (len(books) > 0):
        return jsonify({
            "message": "Books List's ",
            "books": books_list
            })

    return jsonify({"message": "Not Books Found.", "books": books_list})


@app.route('/books/<string:id>')
def getBook(id):
    """
    This route is for get a book for your name.

    Recive the book name por parameter.

    """
    con = connect(db)
    cursor = getCursor(con)

    cursor.execute(f"SELECT * FROM books WHERE(id = {int(id)})")
    bookFound = cursor.fetchall()

    con.commit()
    cursor.close()

    if (len(bookFound) > 0):
        # creating book object for return it
        book = {
                'id': bookFound[0][0],
                'name': bookFound[0][1],
                'price': bookFound[0][2]
                }

        return jsonify({
            "message": "Book Found",
            "book": book

            })

    return jsonify({"message": "Book not Found"})


@app.route('/books', methods=['POST'])
def addBook():
    """
    This is the route for add
    a new book at the database.

    """

    con = connect(db)
    cursor = getCursor(con)

    # creating the book for save in the database
    book = {
            'id': int(request.json['id']),
            'name': request.json['name'],
            'price': request.json['price']
            }


    # esto linea quiza falla porque no le estamos pasando el id
    cursor.execute("INSERT INTO books VALUES({}, {}, {})".format(book['id'], book['name'], book['price']))
    cursor.execute("SELECT * FROM books")
    # getting the new list of books for return it
    new_books = cursor.fecthall()

    con.commit()
    cursor.close()


    # getting the new list but in objects
    new_books_list = [{'id': new[0], 'name': new[1], 'price': new[2]} for new in new_books]

    return jsonify({
        "message": "Book Added Sucessfully",
        "bookAdded": book,
        "newBooks": new_books_list
        })


@app.route('/books/<string:id>', methods=['DELETE'])
def deleteBook(id):
    """
    This is the route for delete
    a book of the database.

    Recive the id of the book for delete.

    """
    con = connect(db)
    cursor = con.cursor(con)

    cursor.execute(f"DELETE FROM books WHERE(id = {id})")

    cursor.execute("SELECT * FROM books")
    books_list = cursor.fecthall()

    con.commit()
    cursor.close()

    new_books_list = [{'id': new[0], 'name': new[1], 'price': new[2]} for new in books_list]

    return jsonify({
        "message": f"Book with id {id} Deleted Sucessfully",
        "new_books_list": new_books_list
        })


@app.route('/books/<string:id>', methods=['PUT'])
def updateBook(id):
    """
    This is the route for update
    a book of the database.

    Recive the id of the book for update.

    """
    con = connect(db)
    cursor = getCursor(con)

    cursor.execute(f"SELECT * FROM BOOKS WHERE(id = {id})")

    # getting the old product
    old_product = cursor.fetchhall()

    cursor.execute(f"UPDATE books SET name = {request.json['name']} WHERE id = {id}")
    cursor.execute(f"UPDATE books SET price = {request.json['price']} WHERE id = {id}")

    cursor.execute(f"SELECT * FROM books WHERE(id = {id})")
    # getting the new product
    new_product = cursor.fetchall()


    con.commit()
    cursor.close()

    return jsonify({
        "message": f"Product with id {id} Updated Sucessfully",
        "old_product": {'id': old_product[0][0], 'name': old_product[0][1], 'price': old_product[0][2]},
        "new_product": {'id': new_product[0][0], 'name': new_product[0][1], 'price': new_product[0][2]}

        })



if __name__ == '__main__':
    app.run(port = 6000, debug = True)
