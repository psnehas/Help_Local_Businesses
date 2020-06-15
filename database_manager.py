"""This module is used to manage various functions regarding interactions with the database"""

import sqlite3

class Book:
    """Contains information about books that will be inserted into the database"""
    def __init__(self, title, year, author, store):
        self.title = title
        self.year = year
        self.author = author
        self.store = store

class SQLiteConnection:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        """Establishes the connection to the database"""
        try:
            self.conn = sqlite3.connect('books.db')
        except exception as e:
            print(e)

    def create_table(self, title):
        """This is used to create a new table in the database"""
        cur = self.conn.cursor
        cur.execute('''CREATE TABLE IF NOT EXISTS book_list (
                        ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT_NULL,
                        author TEXT NOT_NULL,
                        year INTEGER NOT_NULL,
                        storename TEXT NOT_NULL
                    )
                    ''')
        self.conn.commit()

    def insert_entry(self, book):
        """Inserts a book object entry into the database"""
        cur = self.conn.cursor()
        cur.execute("insert into book_list values (?, ?, ?, ?, ?)", (None, book.title, book.author, book.year, book.store))
        self.conn.commit()

    def select_all_entries(self):
        """Selects all entries from the book list"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM book_list")
        new_books = [Book(row[1], row[3], row[2], row[4]) for row in cur.fetchall()] #List comprehension that contains a list of all of the books in the database converted into book objects
        return new_books


    def select_entries(self, query):
        """Selects specified books from the book list"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM book_list WHERE ?=title OR ?=author OR ?=storename", (query, query, query))
        new_books = [Book(row[1], row[3], row[2], row[4]) for row in cur.fetchall()]
        return new_books

    def delete_all_entries(self):
        """Clears the entire table of entries"""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM book_list")
        self.conn.commit()

    def delete_entry(self, book):
        """Deletes given book from the database"""

        cur = self.conn.cursor()
        if isinstance(book, Book):
            cur.execute("DELETE FROM book_list WHERE title=? AND store=?", (book.title, book.store))
        elif isinstance(book, str):
            cur.execute("DELETE FROM book_list WHERE title=? OR author=?", (book, book))
        self.conn.commit()

    def close_connection(self):
        """Closes the connection after making changes"""
        self.conn.close()

hi = SQLiteConnection()
hi.select_all_entries()