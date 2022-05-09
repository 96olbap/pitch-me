from . import db

class User(db.Model):
    '''
    User class that will define user objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    # email = db.Column(db.String(255),unique= True, index = True)
    # bio =db.Column(db.String(255))
    # profile_pic_path = db.Column(db.String())
    # pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

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