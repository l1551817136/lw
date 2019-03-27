from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
class User(db.Model):   
    __tablename__ = 'users'   
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)   
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)      
    def __repr__(self):        
       return '<User %r,Role id %r>' %(self.username,self.role_id)
    
class Role(db.Model):    
    __tablename__ = 'roles'    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    name = db.Column(db.String(16), nullable=False, unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')        
    def __repr__(self):        
         return '<Role %r>' % self.name    
db.drop_all()         
db.create_all()
admin_role =Role(name='Admin') 
mod_role = Role(name='Moderator') 
user_role = Role(name='User') 
user_john = User(username='john', role=admin_role) 
user_susan = User(username='susan', role=user_role) 
user_david = User(username='david', role=user_role)
db.session.add(admin_role) 
db.session.add(mod_role) 
db.session.add(user_role)
db.session.add(user_john) 
db.session.add(user_susan) 
db.session.add(user_david)
db.session.commit() 
admin_role.name = 'Administrator' 
db.session.add(admin_role) 
db.session.commit()