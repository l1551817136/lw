from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/') 
def index(): 
   return render_template('index.html') 
@app.route('/user/<name>') 
def user(name): 
   dit = {"wang":521,"li":340}
   return render_template('user.html', comments=dit )
if __name__ == "__main__":
    app.run(debug = True)
    # 加个注释