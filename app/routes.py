from flask import render_template, url_for, flash, redirect
from app import app, db, bycrypt
from app.models import User
from flask import request


@app.route("/")
@app.route("/home")
def home():
    return "Welcome to the Web Monitoring App"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        hashed_password = bycrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, phone_number=phone_number, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You can now login.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

