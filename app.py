from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html"),"assets\profile.profile.jpg"


@app.route("/about.html")
def about():
    skills = {"Front-End developer.","Machine Learning.","Graphic Desginig.","Problem Sloving."}
    return render_template("about.html", skills = skills)

@app.route("/index.html")
def index():
    return render_template("index.html"),"assets\profile.profile.jpg"

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/resume.html")
def resume():
    return render_template("resume.html")
    

if __name__ == "__main__":
    app.run(debug = True)