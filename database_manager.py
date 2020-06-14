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
        try:
            self.conn = sqlite3.connect('books.db')
        except exception as e:
            print(e)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS book_list (
                        ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT_NULL,
                        author TEXT NOT_NULL,
                        year INTEGER NOT_NULL,
                        storename TEXT NOT_NULL
                    )
                    ''')
        self.conn.commit()

    def insert_entry(self, book):
        self.c.execute("insert into book_list values (?, ?, ?, ?, ?)", (None, book.title, book.author, book.year, book.store))
        self.conn.commit()

    def select_all_entries(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM book_list")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def delete_all_entries(self):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM book_list")
        self.conn.commit()
