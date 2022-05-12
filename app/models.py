from datetime import datetime
from unicodedata import category

from click import option
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    load_user function to retrieve a user when a unique identifier is passed
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    User class that will define user objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique= True, index = True)
    bio =db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitch = db.relationship('Pitch', backref = 'pitch', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User { self.username }'

class Role(db.Model):
    '''
    Role class that will define role objects
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    '''
    Pitch class that will generate new instances of pitch objects
    '''
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    message = db.Column(db.String(255), nullable = False)
    like = db.Column(db.Integer)
    dislike = db.Column(db.Integer)
    author = db.Column(db.String(80), nullable = False)
    category = db.Column(db.String(), nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))