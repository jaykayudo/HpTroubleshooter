from flask import  flash, session,redirect,url_for,request
from settings import app
with app.app_context():
    def login_required(func):
    
        if not "user" in session:
            flash("You are not an expert","error")
            return redirect(url_for("login"))
        else:
            return func


