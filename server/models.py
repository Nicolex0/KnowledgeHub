from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    prof_pic = db.Column(db.String)
    join_date = db.Column(db.DateTime)

    # Relationship mapping the user to related comments
    comments = db.relationship("Comment", back_populates="user", cascade = "all, delete-orphan")

    # Association proxy to get article for this user through comments
    article = association_proxy("comments", "article", creator=lambda article_obj: Comment(article=article_obj))

    #Serialize
    serialize_rules = ("-comments.user",)

    def __init__(self, name, email, password = None, join_date=None, prof_pic=None, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.join_date = join_date
        self.prof_pic = prof_pic

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
        


    def __repr__(self):
        return f"<User {self.id}, {self.name}, {self.email}, {self.password}>"

class Article(db.Model, SerializerMixin):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    creation_date = db.Column(db.DateTime)

    # Relatonship mapping article to related comments
    comments = db.relationship("Comment", back_populates = "article", cascade = "all, delete-orphan")

    # Association proxy to get users for this article through comments
    user = association_proxy("comments", "user", creator=lambda user_obj: Comment(user=user_obj))

    #Serialize
    serialize_rules = ("-comments.article",)

    def __init__(self, title, creation_date, id=None):
        self.id = id
        self.title = title
        self.creation_date = creation_date
    
    def __repr__(self):
        return f"<{self.id}, {self.title}, {self.creation_date}>"

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    creation_date = db.Column(db.DateTime)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"))

    # Relationship mapping the comments to related user
    user = db.relationship("User", back_populates="comments")

    # Relationship mapping the comments to article
    article = db.relationship("Article", back_populates = "comments")

    def __init__(self, content, creation_date, id=None):
        self.id = id
        self.content = content
        self.creation_date = creation_date

    def __repr__(self):
        return f"<Comment {self.id}, {self.content}, {self.creation_date}>"








    


