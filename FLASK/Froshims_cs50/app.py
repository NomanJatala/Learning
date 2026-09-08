
from cs50 import SQL 
from flask import Flask, render_template, request, redirect

app  = Flask(__name__)

db = SQL("sqlite:///froshims.db")


SPORTS = [
     "Basketball",
     "Soccer",
     "Ultimate Frisbee"
]


@app.route("/",methods=["GET","POST"])
def index():
     return render_template("index.html",sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    # name not entered
    if not name:
        return render_template("error.html",message="missing name")

    sports = request.form.getlist("sport")
    # sport not entered
    if not sports:
        return render_template("error.html",message="sport is missing")
    # sport invalid
    for sport in sports:
        if sport not in SPORTS:
            return render_template("error.html",message="Invaid Sport")
    # remember student
    for sport in sports:
        db.execute("INSERT INTO registrants (name, sport) VALUES(?,?)",name,sport)

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    # showing registrants
    registrants = db.execute("SELECT * FROM registrants") 
    return render_template("registrants.html",registrants=registrants)

@app.route("/deregister",methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id=?",id)
    return redirect("/registrants")



app.run(debug=True)


# Data Base creating
'''  
sqlite3 commands

    1. $ sqlite3 froshims.db
    2. > CREATE TABLE registrants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sport TEXT NOT NULL

        );
    3. To check table is created?
       > .table

'''