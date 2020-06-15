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
        books_list_table = '''CREATE TABLE IF NOT EXISTS books_list (
                                        bid INTEGER PRIMARY KEY AUTOINCREMENT,
                                        bookName TEXT NOT_NULL,
                                        authorName TEXT NOT_NULL,
                                        yearPublished INTEGER NOT_NULL,
                                        bookCategory TEXT NOT_NULL,
                                        bookPrice FLOAT NOT_NULL
                                    )
                                    '''
        customer_table = '''CREATE TABLE IF NOT EXISTS customer_data (
                                        cid INTEGER PRIMARY KEY AUTOINCREMENT,
                                        firstName TEXT NOT_NULL,
                                        lastName TEXT NOT_NULL,
                                        customerEmail TEXT NOT_NULL,
                                        customerPassword TEXT NOT_NULL,
                                        customerZipCode INTEGER NOT_NULL
                                    )
                                    '''
        bookseller_table = '''CREATE TABLE IF NOT EXISTS bookseller_data (
                                        bsid INTEGER PRIMARY KEY AUTOINCREMENT,
                                        storeName TEXT NOT_NULL,
                                        storeLocation TEXT NOT_NULL,
                                        storeOwnerName INTEGER NOT_NULL,
                                        storeContactNum TEXT NOT_NULL,
                                        storeOwnerEmail FLOAT NOT_NULL
                                    )
                                    '''
        cur.execute(books_list_table)
        cur.execute(customer_table)
        cur.execute(bookseller_table)

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

    def add_seller(self, seller_details):
        """Adds a book seller to the database"""
        store_name = seller_details[0]
        location = seller_details[1]
        email = seller_details[2]
        name = seller_details[3]
        number = seller_details[4]

        cur = self.conn.cursor()
        cur.execute("insert into bookseller_data values (?, ?, ?, ?, ?, ?)",
                    (None, store_name, location, name, number, email))

        self.conn.commit()

    def select_all_booksellers(self):
        """Prints all the booksellers details"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM bookseller_data")
        rows = cur.fetchall()
        for row in rows:
            print(row)

