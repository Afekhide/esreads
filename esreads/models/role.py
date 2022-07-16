import json
from esreads import db


class Role(db.Model):
    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    users = db.relationship('User', backref='role', lazy='dynamic')
    default = db.Column(db.Boolean, nullable=True, default=0)

