#!/usr/bin/env python3
#encoding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(45), unique=True, nullable=False)
    pwdhash = db.Column("pwdhash", db.String(128), nullable=False)
    role = db.Column("role", db.Integer)

    def __init__(self, username, password, role):
        #self.id = id
        self.username = username
        self.pwdhash = generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return "<User %r>" % self.username

    def verify_password(self, password):
        return check_password_hash(self.pwdhash, password)


if __name__ == '__main__':
    print("models")
