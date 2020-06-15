import sqlite3
from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterBookseller,RegisterCustomer,LoginCustomer
from database_manager import SQLiteConnection
from flask_bootstrap import Bootstrap
app = Flask(__name__)

# followed video tutorials: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=136s,     https://www.youtube.com/watch?v=3mwFC4SHY-Y

Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = 'any secret string'

@app.route('/registerSeller', methods=('GET', 'POST'))
def registerSeller():
    sellerDetails = []
    form = RegisterBookseller()
    for x in form:
        sellerDetails.append(x.data)
    database = SQLiteConnection()
    database.add_seller(sellerDetails)
    database.select_all_booksellers()
    database.close_connection()
    if request.method=='POST':
        return redirect(url_for("loginSeller"))
    return render_template('registerSeller.html',title= "RegisterSeller",form=form)

@app.route('/registerCustomer', methods=('GET', 'POST'))
def registerCustomer():
    customerDetails = []
    form = RegisterCustomer()
    for x in form:
        customerDetails.append(x.data)
    database = SQLiteConnection()
    database.add_seller(customerDetails)
    database.select_all_booksellers()
    database.close_connection()
    if request.method=='POST':
        return redirect(url_for("loginCustomer"))
    return render_template('registerCustomer.html', title="RegisterCustomer", form=form)

@app.route('/loginSeller', methods = ('GET','POST'))
def loginSeller():
    loginDetails = []
    form = LoginCustomer()
    if request.method=='POST':
        return redirect(url_for("loginSeller"))

@app.route('/')
def index():
    return render_template('landingPage.html')  



if __name__ == "__main__":
    app.run(debug=True)
    registerSeller()
