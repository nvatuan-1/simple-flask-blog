from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def get_data(self):
        data = vars(self)
        del data['_sa_instance_state']
        return data

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    title = db.Column(db.String)
    intro_content = db.Column(db.String)
    post_date: db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_data(self):
        data = vars(self)
        del data['_sa_instance_state']
        return data