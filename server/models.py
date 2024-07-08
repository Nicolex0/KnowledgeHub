from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    prof_pic = db.Column(db.String)
    join_date = db.Column(db.DateTime)

    def __init__(self, name, email, password = None, join_date=None, prof_pic=None, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.join_date = join_date
        self.prof_pic = prof_pic

    def password(self):
        pass

    def __repr__(self):
        return f"<User {self.id}, {self.name}, {self.email}, {self.password}>"

class Article(db.Model, SerializerMixin):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    creation_date = db.Column(db.DateTime)

    def __init__(self, title, creation_date, id=None):
        self.id = id
        self.title = title
        self.creation_date = creation_date
    
    def __repr__(self):
        return f"{self.id}, {self.title}, {self.creation_date}"




    


