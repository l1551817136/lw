from flask_script import Manager
from flask import Flask
app = Flask(__name__)
manager = Manager(app)
@app.route("/")
def hello():
   return 'hello world'
if __name__== "__main__":
    manager.run()