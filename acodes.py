# imports

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template

from flask.ext.sqlalchemy import SQLAlchemy

from models import Acode
from a_forms import AcodeForm

import pdb
import csv
import os


# creating the application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# databases init
db = SQLAlchemy(app)

# acode model

'''class Acode(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    resource = db.Column(db.String(100))

    def __init__(self, id, resource):
        self.id = id;
        self.resource = resource;

    def __repr__(self):
        return 'key = {0} resource = {1}'.format(self.id, self.resource)
'''


#db init
def init_db2():
    with open('ocodes_raw.csv', 'rb') as csvfile:
        ocode_read = csv.reader(csvfile, delimiter=',')
        for row in ocode_read:
            print row[0]
            temp_code = Acode(row[0], row[1])
            db.session.add(temp_code)

    db.session.commit()

# db methods
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def front_page():
    return render_template('front.html')

@app.route('/code', methods=['GET'])
def redirect_code():
    form = AcodeForm()
    ocode = request.args['code']
    cur = g.db.execute('select resource from acode where id=?', [ocode])
    redir_url = cur.fetchone()
    if redir_url is None:
        abort(404)
    else:
        return redirect(redir_url[0])
#    return redir_url

if __name__ == '__main__':
    app.run()
