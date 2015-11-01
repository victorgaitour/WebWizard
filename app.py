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

@app.route("/about", methods = ["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/services", methods = ["POST","GET"])
def services():
    return render_template("services.html")

@app.route("/testimonials", methods = ["POST","GET"])
def testimonials():
    return render_template("testimonials.html")

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
    app.run(port=8000)
