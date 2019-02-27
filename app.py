from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "helloooo...."
@app.route("/home")
def home():
    return "WELCOME TO MY HOME PAGE"
@app.route("/contact")
def contact():
    return "contact"
@app.route("/about")
def about():
    return "about"
if(__name__=="__main__"):
    app.run()