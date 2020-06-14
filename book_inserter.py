"""This script wil take a csv file as input and create a book object that contains it's title, author, publishing year, and
the store it is offered at. Then, this book will be inserted as a new entry into the database.
This assumes the title is in the first column, then year, then author, then store"""

from database_manager import Book, SQLiteConnection
import csv

def main():
    file = "MOCK_DATA.csv"
    database = SQLiteConnection() #Opens up a connection to the database

    with open(file, "r", encoding="Latin1") as infile:      #Opens up the csv file to read entries into the database
        infile.readline()
        lines = csv.reader(infile)
        bookstore_list = ["Ma and Pa", "Brick and Mortar", "coolbooks", "bookCity!"]  #Inserts a fake store name into the database, will be real in actual implementation
        count = 0
        for line in lines:
            new_book = Book(line[0], line[1], line[2], bookstore_list[count%4])
            database.insert_entry(new_book)
            count += 1

if __name__ == __main__:
    main()

