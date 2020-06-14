import sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterBookseller
app = Flask(__name__)
# trying to make a function that can be used to create/connect to customers.db, booksellers.db and books.db. 
# then creating three different models for each of the above databases.
# followed video tutorials: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=136s,     https://www.youtube.com/watch?v=3mwFC4SHY-Y
class SQLiteConnection:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('books.db')
        except exception as e:
            print(e)
        self.c = self.conn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = 'any secret string'
# db_customer = SQLAlchemy(app)
# db_bookseller = SQLAlchemy(app)
# db_books = SQLAlchemy(app)

# class CustomerData(db_customer.Model):
#     cid = db_customer.Column(db_customer.Integer, primary_key = True)
#     firstName = db_customer.Column(db_customer.String(200), nullable = False)
#     LastName = db_customer.Column(db_customer.String(200), nullable = False)
#     customerEmail = db_customer.Column(db_customer.String(200))
#     customerPassword = db_customer.Column(db_customer.String(20), nullable = False)
#     customerZipCode = db_customer.Column(db_customer.Integer, nullable = False)

#     def __repr__(self):
#         return '<Task %r>' %self.cid

# class BookSellerData(db_bookseller.Model):
#     bsid = db_bookseller.Column(db_bookseller.Integer, primary_key = True)
#     storeName = db_bookseller.Column(db_bookseller.String(400), nullable = False)
#     storeLocation = db_bookseller.Column(db_bookseller.String(600), nullable = False)
#     storeOwner = db_bookseller.Column(db_bookseller.String(100), nullable = False)
#     storeContactNum = db_bookseller.Column(db_bookseller.Integer)
#     storeOwnerEmail = db_bookseller.Column(db_bookseller.String(100), nullable = False)
    
#     def __repr__(self):
#         return '<Task %r>' %self.bsid
        
# class Books(db_books.Model):
#     bid = db_books.Column(db_books.Integer, primary_key = True)
#     bookName = db_books.Column(db_books.String(200), nullable = False)
#     authorName = db_books.Column(db_books.String(200), nullable = False)
#     bookCategory = db_books.Column(db_books.String(100), nullable = False)
#     bookPrice = db_books.Column(db_books.Float, nullable = False)




@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterBookseller()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/')
def index():
    return render_template('landingPage.html')  

if __name__ == "__main__":
    app.run(debug=True)