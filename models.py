#from acodes import db
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from acodes import db
#app = Flask(__name__)

#db = SQLAlchemy(app)

class Acode(db.Model):
    __tablename__ = 'acodes'
    id = db.Column(db.String(10), primary_key=True)
    resource = db.Column(db.String(300))

    def __init__(self, id, resource):
        self.id = id;
        self.resource = resource;

    def __repr__(self):
        return 'key = {0} resource = {1}'.format(self.id, self.resource)

