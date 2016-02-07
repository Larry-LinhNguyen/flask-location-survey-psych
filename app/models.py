from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def get_datetime():
    return datetime.utcnow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, default=get_datetime)
    modified = db.Column(db.DateTime, onupdate=get_datetime)
    email = db.Column(db.Unicode(100, collation='utf8_general_ci'), unique = True)
    name = db.Column(db.Unicode(100, collation='utf8_general_ci'))

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, default=get_datetime)
    modified = db.Column(db.DateTime, onupdate=get_datetime)
    data = db.Column(db.Unicode(1000, collation='utf8_general_ci'))

# TODO
# call this somewhere in application.py/home, run and open home page
# then check if db is created and then remove it
#
def create_db():
    db.create_all()
