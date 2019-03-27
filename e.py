from flask import Flask, render_template, session, redirect, url_for 
from flask_bootstrap import Bootstrap
from flask_wtf import Form 
from wtforms import StringField, SubmitField 
from wtforms.validators import Required 
class NameForm(Form): 
   name = StringField('What is your name?', validators=[Required()])
   submit = SubmitField('Submit')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app) 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
  form = NameForm() 
  if form.validate_on_submit(): 
    session['name'] = form.name.data 
    return redirect(url_for('index')) 
  return render_template('index.html', form=form, name=session.get('name'))
if __name__ == '__main__':
    app.run(debug=True)
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