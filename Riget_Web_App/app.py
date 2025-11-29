from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = "Database.db"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/educational")
def educational_page():
    return render_template("educational.html")

@app.route("/booking", methods=['GET', 'POST'])
def booking_page():
    return render_template("booking.html")

# @app.route('/register', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)

