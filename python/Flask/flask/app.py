from flask import Flask
"""it create a instace of flak class , which 
will be your wsgi (web server gateway interface)appplication"""


# WSGI Application
app= Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to flask app by khushal"
@app.route("/index")
def index():
    return "This is a index page which is used to test the flask app by khushal patel"

if __name__ == "__main__":
    app.run(debug=True)
    