"""
SDEV 300
Author: Charlemagne Marc
File: marc_charlemagne_lab5
Date: 02/20/2023
Lab Week 6
Purpose: Python program that allows a user to load Flask website regarding a Soccer Coach
"""
import sqlite3
import re
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

# initialize Flask app
app = Flask(__name__)

# set up session secret key
app.secret_key = 'super secret key'

def get_db():
    """
    get_db(): creates database connection and table
    return: conn: database connection
    """
    conn = sqlite3.connect('users.db')

    # create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL);""")

    # commit changes to the database
    conn.commit()

    return conn


def get_date():
    """
    get_date(): function that returns the current date (Month Day, Year)
    """
    # get current date
    today = datetime.today()
    date = today.strftime("%B %d, %Y")

    return date


@app.route("/")
def index():
    """
    index(): function that returns render template of index html
    return: index.html: name of html file for index
    """
    name = "Charlemagne Marc"
    date = get_date()
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('index.html', name=name, date=date, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    login(): login page route
    return: render_template: login.html, name
    """
    name = "Charlemagne Marc"
    # check if user is already logged in
    if 'user_id' in session:
        return redirect('/')
    # if user is not logged in, check if form is submitted
    if request.method == 'POST':
        # get form data
        username = request.form['username']
        password = request.form['password']
        # connect to database
        conn = get_db()
        cur = conn.cursor()
        # execute query to get user with given username
        cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cur.fetchone()
        # check if user exists and password is correct
        if user is not None and check_password_hash(user[2], password):
            # set user ID in session
            session['user_id'] = user[0]
            # redirect to home page
            return redirect('/')
        # display error message
        error = 'Invalid username or password'
        return render_template('login.html', error=error, name=name)
    # if form is not submitted, display login page
    return render_template('login.html', name=name)


def valid_password(password):
    """
    valid_password(password): checks to see if string is a valid password
    A password complexity should be enforced to include at least 12 characters in length, and
    include at least 1 uppercase character, 1 lowercase character, 1 number and 1 special character.
    return: boolean: boolean on validicity of password
    """
    # check for length
    if len(password) < 12:
        print("check length")
        return False
    # check for upper
    if not re.search(r"[A-Z]", password):
        print("no upper")
        return False
    # check for lower
    if not re.search(r"[a-z]", password):
        print("no lower")
        return False
    # check for digit
    if not re.search(r"\d", password):
        print("no digit")
        return False
    # check for special
    if not re.search(r"[@_!#$%^&*()<>?/|}{~:]", password):
        print("no special")
        return False
    # return True since passes all conditions
    return True


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    register(): registration page route
    return: page route based on conditions
    """
    name = "Charlemagne Marc"
    # check if user is already logged in
    if 'user_id' in session:
        return redirect('/')
    # if user is not logged in, check if form is submitted
    if request.method == 'POST':
        # get form data
        username = request.form['username']
        password = request.form['password']
        # if password is not valid error message and redirect to registration
        if not valid_password(password):
            # display error message
            error = 'Invalid password.'
            return render_template('registration.html', error=error, name=name)
        # generate password hash
        password_hash = generate_password_hash(password)
        # connect to database
        conn = get_db()
        cur = conn.cursor()
        # execute query to insert user into database
        cur.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                    (username, password_hash))
        conn.commit()
        # redirect to login page
        return redirect('/login')
    # if form is not submitted, display registration page
    return render_template('registration.html', name=name)


@app.route('/logout')
def logout():
    """
    logout(): logout page route
    return: redirect: to login page
    """
    # remove user ID from session
    session.pop('user_id', None)
    # redirect to login page
    return redirect('/login')


@app.route('/roster')
def roster():
    """
    roster(): roster page route
    return: render template: roster.html or redirect to login page
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("roster.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/about')
def about():
    """
    about(): function that returns render template of about html
    return: about.html: name of html file for about
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("about.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/philosophy')
def philosophy():
    """
    philsophy(): function that returns render template of philosophy html
    return: philosophy.html: name of html file for philosophy
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("philosophy.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/players_expectations')
def players_expectations():
    """
    players_expectations(): function that returns render template of players html
    return: players.html: name of html file for players
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("players.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/parents_expectations')
def parents_expectations():
    """
    parents_expectations(): function that returns render template of parents html
    return: parents.html: name of html file for parents
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("parents.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/contact')
def contact():
    """
    contact(): function that returns render template of contact html
    return: contact.html: name of html file for contact
    """
    name = "Charlemagne Marc"
    # check if user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template("contact.html", name=name, user_id=user_id)
    # if user is not logged in, redirect to login page
    return redirect('/login')


@app.route('/admin')
def admin():
    """
    admin(): function that returns a redirect to index 
    return: url_for: index url
    """
    return redirect((url_for("index")))


# run app
if __name__ == "__main__":
    app.run(debug=True)
