import os
from werkzeug.utils import secure_filename
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder="Templates")

@app.route("/", methods=["POST", "GET"])
def home():
    thenodes=[]
    i=0
    while(i<3):
        thenodes+=[getnode()]
        i+=1
        render_template("Home.html")
    print(thenodes)
    return render_template("Home.html")


def getnode():
    if request.method=="POST" :
        return request.form["n"]

#///////////////////////////////

if __name__ =="__main__":
    app.run()

