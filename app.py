from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session

app = Flask('__name__')
app.config['SECRET_KEY'] = "Alex is great"

@app.route("/", methods = ["POST", "GET"])
@app.route("/home", methods = ["POST", "GET"])
def home():
    name= ""
    email=""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
    print name
    print email
    return render_template("home.html")

@app.route("/index", methods = ["POST", "GET"])
def index():
   return render_template("index.html")

@app.route("/stuff1", methods = ["POST","GET"])
def stuff1():
    return "stuff1"
@app.route("/stuff2", methods = ["POST","GET"])
def stuff2():
    return "stuff2"
@app.route("/stuff3", methods = ["POST","GET"])
def stuff3():
    return "stuff3"

@app.route("/testbase")
def testbase():
    return render_template("base.html")


@app.route("/signup", methods = ["POST", "GET"])
def signup():
    name= ""
    email=""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
    print name
    print email
    return render_template("signup.html")

if __name__=="__main__":
    app.debug = True
    app.run()
