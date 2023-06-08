#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from engine.db_config import SQLALCHEMY_DATABASE_URI
from engine.db_mod import add_user
from engine.database import db, User


app = Flask(__name__)
app.secret_key = 'learnhub'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

#Route for home
@app.route('/')
def home():
    return render_template('html/home.html')

# Routes for authentication

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        account_type = request.form['account_type']

        #check if theres already an account using the provided email
        exist = User.query.filter_by(email=email).first()
        if exist:
            flash("Email already exists")
            return redirect('/login')

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Create a new User object
        user = User(first_name=first_name, last_name=last_name, email=email,
                    password=hashed_password, phone_number=phone_number, account_type=account_type)

        # Add the user to the database
        add_user(user)

        return redirect('/login')

    return render_template('html/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the user with the provided email
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # User is authenticated, store user ID in the session
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            # Invalid credentials, display an error message
            error_message = 'Invalid email or password'
            return render_template('login.html', error_message=error_message)

    return render_template('html/login.html')

@app.route('/logout')
def logout():
    # Clear the user ID from the session
    session.pop('user_id', None)
    return redirect('/login')

# Other routes and views

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect('/login')

    # Retrieve the user from the database
    user = User.query.get(session['user_id'])

    return render_template('html/dashboard.html', user=user)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
