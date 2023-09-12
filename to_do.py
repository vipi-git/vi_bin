from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_area = db.Column(db.String(100))
    task_project = db.Column(db.String(100))
    task_name = db.Column(db.String(100))
    due_date = db.Column(db.String(20))
    priority = db.Column(db.String(20))
    completion_date = db.Column(db.String(20))
    remark = db.Column(db.String(100))

db.create_all()
