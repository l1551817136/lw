from flask import request,Flask
app=Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent
if __name__ == "__main__":
    app.run(debug = True)