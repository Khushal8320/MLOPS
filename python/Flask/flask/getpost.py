from flask import Flask, render_template, request, redirect, url_for
"""it create a instace of flak class , 
which is the main class of flask framework and it takes the name of the module as an argument"""

### jinja 2 template engine
#{{expression}} --- used to print the value of the variable
#{% statement %} --- used to write the control flow statements like if, for, etc.    
#{# comment #} --- used to write the comments in the template

getpost = Flask(__name__)
@getpost.route("/")
def welcome():
    return render_template("home.html")
@getpost.route("/about")
def about():
    return render_template("about.html")
@getpost.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"Hello, {name}! Your email is {email}. Welcome to the Flask app."
    return render_template("form.html")

@getpost.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"Hello, {name}! Your email is {email}. Welcome to the Flask app with submit."
    return render_template("form.html")
@getpost.route("/success/<int:score>")
def success(score):
    
    result1 = ""
    if score >= 80:
        result1 = "Congratulations! You passed with flying colors!"
    else:
        result1 = "Sorry, you did not pass. Better luck next time!"
    return render_template("result.html", result =result1)

@getpost.route("/successer/<int:score>")
def successer(score):
    
    result2 = score
    
    if score >= 80:
        result2 = "Congratulations! You passed with flying colors!"
    else:
        result2 = "Sorry, you did not pass. Better luck next time!"
    
    exp = {'score':score, 'result':result2}
    return render_template("result1.html", results=exp)

@getpost.route("/successerifelse/<int:score>")
def succeserifelse(score):
    
   
    return render_template("result2.html", score=score)

@getpost.route("/subjects", methods=["GET","POST"])
def subjects():
    if request.method == "POST":
        sub1 = float(request.form["sub1"])
        sub2 = float(request.form["sub2"])
        sub3 = float(request.form["sub3"])
        sub4 = float(request.form["sub4"])
        total = (sub1 + sub2 + sub3 +sub4)/4  
    else:
        return render_template("subjects.html")
    return redirect(url_for("successer", score=total))
if __name__ == "__main__":
    getpost.run(debug=True)
    

