from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from settings import app
import hashlib
from sqlalchemy.sql import func



db = SQLAlchemy(app)

class Admin(db.Model):
    __tablename__="admin"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def set_password(self, password):
        salt = "dinero"
        gen_pass = password + salt
        hashed_pass = hashlib.md5(gen_pass.encode())
        self.password = hashed_pass.hexdigest()
    def check_password(self,password):
    	salt = "dinero"; gen_pass = password + salt;hashed_pass = hashlib.md5(gen_pass.encode());return self.password == hashed_pass.hexdigest()

def save(self):
	db.session.add(self)
	db.session.commit()
def __repr__(self):
    return f'<Admin "{self.email}">'
		
class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    def __repr__(self):
        return f'<Issue "{self.title}">'
    def save(self):
    	db.session.add(self);db.session.commit(); return self

issue_solution = db.Table('issue_solution',
                    db.Column('solution_id', db.Integer, db.ForeignKey('solutions.id')),
                    db.Column('issue_id', db.Integer, db.ForeignKey('issues.id'))
                    )
    
class Solution(db.Model):
    __tablename__ = "solutions"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    issues = db.relationship("Issue",secondary=issue_solution,backref="solutions")
    steps = db.relationship('Step', backref='solutions')
    def __repr__(self):
        return f'<Solution "{self.name}">'
    def save(self):
        db.session.add(self);db.session.commit(); return self
class Step(db.Model):
    __tablename__ = "steps"

    id = db.Column(db.Integer, primary_key = True)
    solution_id = db.Column(db.Integer,db.ForeignKey('solutions.id'))
    step = db.Column(db.String)
    order = db.Column(db.Integer)
    def __repr__(self):
    	return f"<Step {self.step} >"
    def save(self):
    	db.session.add(self);db.session.commit(); return self
	
    
def minor_save():
    db.session.commit()

with app.app_context():
	db.create_all()