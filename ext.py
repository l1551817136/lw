from flask.ext import script 
manager = Manager(app)

@app.route("/")
def hello():
   return 'hello world'
if __name__== "__main__":
    manager.run()