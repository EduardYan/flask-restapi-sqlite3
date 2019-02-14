"""
This is the principal file
for execute the server.

The server is in port 6000.

"""

from flask import Flask, jsonify, request
from sqlite3 import connect


app = Flask(__name__)

try:
    # getting the conection of the database
    con = connect('database/books.db')

except:
    print('Some error in the connection.')


def getCursor(con):
    """
    Return the cursor of the connection
    passed for parameter.

    """
    return con.cursor()


@app.route('/books')
def getBooks():
    """
    This route is for get
    the books of the database.

    Return the list of books, in the database.

    """
    cursor = getCursor(con)
    cursor.execute("SELECT * FROM books")

    books_list = cursor.fecthall()

    cursor.commit()

    print(books_list)

    return jsonify({
        "message": "Books List's ",
        "books": books_list
        })


@app.route('/book/<string:book_name>')
def getBook(book_name):

    cursor = genCursor(con)
    cursor.execute(f"SELECT name FROM books WHERE(name = {book_name})")

    book = cursor.fecthall()

    cursor.commit()

    print(book)

    return jsonif({
        "message": "Book Found",
        "book": book

        })



@app.route('/books', methods=['POST'])
def addBook():
    cursor = getCursor(con)

    # creating the book for save in the database
    book = {
            'name': request.json['name'],
            'price': request.json['price']
            }


    # esto linea quiza falla porque no le estamos pasando el id
    # ya vere que hago para solucionarlo
    cursor.execute(f"INSERT INTO books VALUES({book['name']}, {book['price'])}")
    new_books_list = cursor.fecthall()

    cursor.commit()

    return jsonify({
        "message": "Book Added Sucessfully",
        "bookAdded": book,
        "newBooks": new_books_list
        })


@app.route('/books/<string:id>', methods=['DELETE'])
def deleteBook(id):
    cursor = getCursor(con)

    cursor.execute(f"DELETE * FROM books WHERE(id = {id})")
    bookDeleted = cursor.fecthall()

    cursor.execute("SELECT * FROM books")
    new_books_list = cursor.fecthall()

    cursor.commit()

    return jsonify({
        "message": f"Book with id {id} Deleted Sucessfully",
        "new_books_list": new_books_list
        })


if __name__ == '__main__':
    app.run(port = 6000, debug = True)
