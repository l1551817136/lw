SECRET_KEY = 'flaskMysql'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@host:port/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True 



from flask import Flask, render_template, jsonify
from db_mysql import db 
app = Flask(__name__)
app.config.from_object('config')
with app.app_context(): 
    db.init_app(app) 
    db.create_all() 



from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy() 
class User(db.Model):   
    __tablename__ = 'users'   
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)   
    role_id = db.Column(db.Integer, nullable=False, server_default='0')     
    def __init__(self,username,role_id):        
        self.username = username        
        self.role_id = role_id     
    def __repr__(self):        
        return '<User %r,Role id %r>' %(self.username,self.role_id) 
class Role(db.Model):    
    __tablename__ = 'roles'    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)     
    def __init__(self,name):        
         self.name = name     
         def __repr__(self):        
            return '<Role %r>' % self.name 

            
User.query.join(Role).filter(Users.username.like('%xx%'))