"""This is a file for do some querys at database."""

from sqlite3 import connect

con = connect('books.db')

cursor = con.cursor()

cursor.execute('select * from books where(name = "other other")')
bookFound = cursor.fetchall()


con.commit()
cursor.close()

if len(bookFound) > 0:
    book = {
            'id': bookFound[0][0],
            'name': bookFound[0][1],
            'price': bookFound[0][2]
            }

    print(book)

else:
    print('not book found')
