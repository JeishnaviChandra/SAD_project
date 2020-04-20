from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model) :

    __tablename__="users"

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=True)
    dob = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, password, dateOfBirth, gender) :

        self.name = name
        self.email = email
        self.password = password
        self.dob = dateOfBirth
        self.gender = gender
        self.timestamp = datetime.now()

class Book(db.Model) :

    __tablename__="books"

    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)

    def __init__(self, isbn, title, author, year) :
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) :

        return "ISBN : " + self.isbn + " | Title : " + self.title + " | Author : " + self.author + " | Year : " + self.year
