from flask import Flask, render_template
"""it create a instace of flak class , 
which is the main class of flask framework and it takes the name of the module as an argument"""
main = Flask(__name__)
@main.route("/")
def welcome():
    return render_template("home.html")
@main.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    main.run(debug=True)

