"""
** Name: ** webpage.py*
** Created on ** 29 Januar 2019*
** Author: ** Nils Arne Topland*
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()

