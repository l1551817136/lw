from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy() 
class User(db.Model):   
    __tablename__ = 'users'   
    id = db.Column(db.Integer, nullable=False, primary_key=True)   
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)   
    role_id = db.Column(db.Integer, nullable=False)     
    def __init__(self,username,role_id):        
        self.username = username        
        self.role_id = role_id     
    def __repr__(self):        
        return '<User %r,Role id %r>' %(self.username,self.role_id) 
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
class Role(db.Model):    
    __tablename__ = 'roles'    
    id = db.Column(db.Integer, nullable=False, primary_key=True)   
    name = db.Column(db.String(16), nullable=False, unique=True)     
    def __init__(self,name):        
         self.name = name     
         def __repr__(self):        
            return '<Role %r>' % self.name 
    users = db.relationship('User', backref='role') 
