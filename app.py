"""
SDEV 300
Author: Charlemagne Marc
File: marc_charlemagne_lab5
Date: 02/20/2023
Lab Week 6
Purpose: Python program that allows a user to load Flask website regarding a Soccer Coach
"""
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    """
    index(): function that returns render template of index html
    return: index.html: name of html file for index
    """
    return render_template("index.html")


@app.route('/about')
def about():
    """
    about(): function that returns render template of about html
    return: about.html: name of html file for about
    """
    return render_template("about.html")


@app.route('/select')
def select_info():
    """
    select_info(): function that returns render template of select html
    return: select.html: name of html file for select
    """
    return render_template("select.html")


@app.route('/players_expectations')
def players_expectations():
    """
    players_expectations(): function that returns render template of players html
    return: players.html: name of html file for players
    """
    return render_template("players.html")


@app.route('/parents_expectations')
def parents_expectations():
    """
    parents_expectations(): function that returns render template of parents html
    return: parents.html: name of html file for parents
    """
    return render_template("parents.html")


@app.route('/contact')
def contact():
    """
    contact(): function that returns render template of contact html
    return: contact.html: name of html file for contact
    """
    return render_template("contact.html")


@app.route('/admin')
def admin():
    """
    admin(): function that returns a redirect to index 
    return: url_for: index url
    """
    return redirect((url_for("index")))


if __name__ == "__main__":
    app.run()
