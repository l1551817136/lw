from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
from flask_migrate import Migrate,MigrateCommand
import config
from flask_wtf import Form 
from wtforms import StringField, SubmitField 
from wtforms.validators import Required 

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)
manager.add_command("shell", Shell(make_context = make_shell_context))
class NameForm(Form): 
   name = StringField('What is your name?', validators=[Required()])
   submit = SubmitField('Submit')
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

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        #form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'),known = session.get('known',False))

if __name__ == '__main__':
    manager.run()