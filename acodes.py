from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask.ext.sqlalchemy import SQLAlchemy

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
    from models import Acode

    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

    with open('ocodes_raw.csv', 'rb') as csvfile:
        ocode_read = csv.reader(csvfile, delimiter=',')
        for row in ocode_read:
            print row[0]
            temp_code = Acode(row[0], row[1])
            db.session.add(temp_code)
            db.session.commit()

# db methods
#def connect_db():
#    return sqlite3.connect(app.config['DATABASE'])

#@app.before_request
#def before_request():
#    g.db = connect_db()

#@app.teardown_request
#def teardown_request(exception):
#    db = getattr(g, 'db', None)
#    if db is not None:
#        db.close()

@app.route('/')
def index():
    from a_forms import AcodeForm
    form = AcodeForm()
    return render_template('front.html', form=form)

@app.route('/code', methods=['GET'])
def redirect_code():

    from a_forms import AcodeForm
    from models import Acode
    form = AcodeForm()
    ocode = request.args['code']
    redir_url = Acode.query.filter_by(id=ocode).first()
    if redir_url is None:
        abort(404)
    else:
        return redirect(redir_url.resource)
#    return redir_url

if __name__ == '__main__':
    app.run()
