# import all the things!
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash
from contextlib import closing

# config ahoy
DATABASE = 'db/freshmeet.db'
DEBUG = True
SECRET_KEY = 'supersecret'
USERNAME = 'admin'
PASSWORD = 'password'

# make rocket ship go
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    # print "hello"
    app.run()

@app.route('/reservations', methods=['POST'])
def add_reservation():
    g.db.execute('INSERT INTO reservations (reservation_id, room_id, start_time, end_time, host, num_attendees, description) values (?, ?)',
                 [request.form['reservation_id'], request.form['room_id'], request.form['start_time'], request.form['end_time'], 
                 request.form['host'], request.form['num_attendees'], request.form['description']])
    g.db.commit()
    flash('Your room reservation has been made.')
    return redirect(url_for('show_entries'))

