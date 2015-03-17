#from acodes import db
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db = SQLAlchemy(app)

class Acode(db.Model):
    __tablename__ = 'acodes'
    id = db.Column(db.String(5), primary_key=True)
    resource = db.Column(db.String(100))

    def __init__(self, id, resource):
        self.id = id;
        self.resource = resource;

    def __repr__(self):
        return 'key = {0} resource = {1}'.format(self.id, self.resource)

