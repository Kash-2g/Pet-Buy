from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True)

    # One-to-many relationship with Buy
    Buys = db.relationship('Buy', backref='user', lazy=True)

   

    serialize_rules = ( "-Buys.user",)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
class Buy(db.Model, SerializerMixin):
    __tablename__ = 'Buys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String)
    address = db.Column(db.String)
    contacts = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Foreign key to users table

    def __repr__(self):
        return f"<Buy(id={self.id}, name='{self.name}')>"


class Breeds(db.Model, SerializerMixin):
    __tablename__ = 'breeds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    speciality = db.Column(db.String)
    image = db.Column(db.String)

    # One-to-many relationship with breedDetail
    

    def __repr__(self):
        return f"<breed(id={self.id}, name='{self.name}', email='{self.email}')>"

class Activity(db.Model,SerializerMixin):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))