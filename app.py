from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/select')
def select_info():
    return render_template("select.html")


@app.route('/players_expectations')
def players_expectations():
    return render_template("players.html")


@app.route('/parents_expectations')
def parents_expectations():
    return render_template("parents.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
