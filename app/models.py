from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String, index=True)
    plan = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.DateTime, index=True)
    time = db.Column(db.DateTime, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Request to {}>".format(self.receiver)

