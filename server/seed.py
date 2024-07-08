#!/usr/bin/env python3

# Standard library imports
import datetime
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Article, User
from config import bcrypt

if __name__ == '__main__':

    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        #Delete Tables
        User.query.delete()
        Article.query.delete()

        db.session.add(User(name=fake.name(), email=fake.email(), join_date=datetime.datetime(2024, 7, 8, 11, 30), password = bcrypt.generate_password_hash("1234")))
        db.session.add(User(name=fake.name(), email=fake.email(), join_date=datetime.datetime(2024, 7, 9, 12, 30), password = bcrypt.generate_password_hash("4567")))
        # db.session.add_all(self)
        
        #Create and add Articles
        db.session.add(Article(title="JS101", creation_date=datetime.datetime(2024, 7, 9)))
        db.session.add(Article(title="Flask101", creation_date=datetime.datetime(2024, 7, 10)))
        db.session.commit()
