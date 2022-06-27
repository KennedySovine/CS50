import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        
        #request info
        message = ""
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        
        #error messages
        if not name:
            message = "Missing name"
        elif not month:
            message = "Missing month"
        elif not day:
            message = "Missing day"

        #add info into db
        db.execute("INSERT INTO birthdays(name, month, day) VALUES(?, ?, ?)", 
        name, 
        month, 
        day, )
        return redirect("/")
                

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        
        return render_template("index.html", birthdays=birthdays)