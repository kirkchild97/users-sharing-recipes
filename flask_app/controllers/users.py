from flask_app import app
from flask import session, request, redirect, flash, render_template, bcrypt
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

b = Bcrypt(app)

@app.route('/')
def start_page():
    return render_template('loginregister.html')

@app.route('/tryregister', methods=['POST'])
def try_register():#Ensure all inputs follow validation protocol before sending to the database
    pass

@app.route('/trylogin', methods=['POST'])
def try_login():#Check for valid user and send to dashboard if successfull
    pass

@app.route('/userDashboard/<user_id>')
def user_dashboard(user_id):#Get all recipes for display on table
    return render_template('dashboard.html')