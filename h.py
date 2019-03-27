from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
from flask_migrate import Migrate,MigrateCommand
import config
from flask_wtf import Form 
from wtforms import StringField, SubmitField 
from wtforms.validators import Required 
import os
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__)
#app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:honoka.cc@222.197.201.131:3306/lw?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flaskMysql'
app.config['DEBUG']= True
app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'liwei@honoka.cc'
app.config['MAIL_PASSWORD'] = 'RuoZhiLi12345'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIT_SENDER'] = 'Flasky Admin <liwei@honoka.cc>'
app.config['FLASKY_ADMIN'] = '1551817136@qq.com'
db = SQLAlchemy(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['FLASKY_MAIT_SENDER'], recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target = send_async_email, args = [app, msg])
    thr.start()
    return thr
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
    sex = db.Column(db.String(64), nullable = True, unique = False, index = True)     
    def __repr__(self):        
       return '<User %r,Role id %r>' %(self.username,self.role_id)
    
class Role(db.Model):    
    __tablename__ = 'roles'    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)   
    name = db.Column(db.String(16), nullable=False, unique=True)
    users = db.relationship('User', backref='role')       
    def __repr__(self):        
         return '<Role %r>' % self.name 
#db.drop_all()
#db.create_all()
@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user',user = user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'),known = session.get('known',False))

if __name__ == '__main__':
    app.run(debug= True)