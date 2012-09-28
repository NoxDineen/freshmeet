# import all the things!
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash, jsonify
from werkzeug.routing import BaseConverter
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

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request():
    d.db.close()


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.route('/<regex("[\d]{4}-[\d]{1,2}-[\d]{1,2}"):day>/')
def list_reservations(day):
    day_reservations = g.db.execute(
        '''SELECT room_id, start_time, end_time, host, num_attendees, description
        FROM reservations 
        WHERE date(start_time) = day OR date(end_time) = day''')
    reservations = [dict(
            room=reservation[0],
            start=reservation[1],
            end=reservation[2],
            host=reservation[3],
            num_attendees=reservation[4],
            description=reservation[5]
            )for reservation in day_reservations.fetchall()]
    return jsonify(reservations)

@app.route('/reservations', methods=['POST'])
def add_reservation():
    g.db.execute('INSERT INTO reservations (reservation_id, room_id, start_time, end_time, host, num_attendees, description) values (?, ?)',
                 [request.form['reservation_id'], request.form['room_id'], request.form['start_time'], request.form['end_time'], 
                 request.form['host'], request.form['num_attendees'], request.form['description']])
    g.db.commit()
    flash('Your room reservation has been made.')
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run()