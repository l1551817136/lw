from app import  db


class User(db.Model):   
    __tablename__ = 'users'   
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)   
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False) 
    性别 = db.Column(db.String(64), nullable = False, unique = True, index = True)     
    def __repr__(self):        
       return '<User %r,Role id %r>' %(self.username,self.role_id)
    
class Role(db.Model):    
    __tablename__ = 'roles'    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    name = db.Column(db.String(16), nullable=False, unique=True)
    users = db.relationship('User', backref=db.backref('role'))       
    def __repr__(self):        
         return '<Role %r>' % self.name 