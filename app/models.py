from . import db

class User(db.Model):
    '''
    User class that will define user objects
    '''
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User { self.username }'