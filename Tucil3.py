from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="Templates")


@app.route("/")
def home():
    return render_template("Home.html")

#///////////////////////////////

if __name__ =="__main__":
    app.run()
