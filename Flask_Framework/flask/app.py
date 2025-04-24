from flask import Flask
# wsgi application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course.\nThis is the best course"

@app.route("/index")
def index():
    return "Hello this is index"





if __name__ == "__main__":
    app.run(debug=True)