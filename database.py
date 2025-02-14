import sqlite3
from book import Book 
import os  

def createDatabase():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        bookId TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        publicationYear TEXT,
        publisher TEXT
    )
    ''')

    conn.commit()
    conn.close()

def saveBookstoDB(bookId, title, author, publicationYear, publisher):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO books (bookId, title, author, publicationYear, publisher)
    VALUES (?, ?, ?, ?, ?)
    ''', (bookId, title, author, publicationYear, publisher))

    conn.commit()
    conn.close()
    os.system("cls" if os.name == "nt" else "clear")

def loadBooksfromDb(library):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    if not rows:
        print("No books available.")
    else:
        for row in rows:
            book = Book(row[0], row[1], row[2], row[3], row[4])
            library.append(book)  

    conn.close()
    os.system("cls" if os.name == "nt" else "clear")

def addSamplebooks():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sample_books = [
        ("1", "Book One", "Author One", "2021", "Publisher One"),
        ("2", "Book Two", "Author Two", "2020", "Publisher Two"),
        ("3", "Book Three", "Author Three", "2022", "Publisher Three")
    ]

    cursor.executemany('''INSERT OR IGNORE INTO books (bookId, title, author, publicationYear, publisher)
                    VALUES (?, ?, ?, ?, ?)''', sample_books)

    conn.commit()
    conn.close()
