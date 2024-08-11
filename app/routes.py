from flask import render_template, url_for, flash, redirect
from app import app, db, bycrypt
from app.models import User
from flask import request


@app.route("/")
@app.route("/home")

def home():
    return "Welcome to the Web Monitoring App"
