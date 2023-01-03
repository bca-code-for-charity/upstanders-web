#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/be_a_friend')
def be_a_friend():
    return render_template("be_a_friend.html")


@app.route('/past_events')
def past_events():
    return render_template("past_events.html")


@app.route('/interest_form')
def interest_form():
    return render_template("interest_form.html")


@app.route('/upcoming_events')
def upcoming_events():
    return render_template("upcoming_events.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
