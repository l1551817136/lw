from flask import Flask, render_template, jsonify
from mysql import db 
app = Flask(__name__)
app.config.from_object('config')
with app.app_context(): 
   db.init_app(app) 
   db.create_all()