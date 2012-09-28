# import all the things!
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

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request():
    d.db.close()

@app.route('/')
def show_schedule():
    cur = g.db.execute('select room_id, name, capacity, type, num_whiteboards from rooms order by type, room_id')
    rooms = [dict(id=row[0], name=row[1], capacity=row[2], type=row[3], num_whiteboards=row[4]) for row in cur.fetchall()]
    return render_template('index.html', rooms = rooms)

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
    return render_template('TEMPLATE_NAME_HERE', reservations=reservations)

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
    init_db()
