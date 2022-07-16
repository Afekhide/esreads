import json
from datetime import datetime
from esreads import db


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    user_email = db.Column(db.String(50), db.ForeignKey('user.email'))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, author={self.user_email})'

