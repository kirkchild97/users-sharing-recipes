from flask_app import app
from flask import session, request, redirect, flash, render_template
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

b = Bcrypt(app)

@app.route('/')
def start_page():
    return render_template('loginregister.html')

@app.route('/tryregister', methods=['POST'])
def try_register():#Ensure all inputs follow validation protocol before sending to the database
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'con_password' : request.form['con_password']
    }
    if User.validate_user_data(data) and User.check_for_email(data):
        data['password'] = b.generate_password_hash(data['password'])
        User.save_user(data)
        print('Success')
    else:
        print('Failed')
    return redirect('/')
    

@app.route('/trylogin', methods=['POST'])
def try_login():#Check for valid user and send to dashboard if successfull
    data = {
        'email' : request.form['email']
    }
    data = User.get_user_login(data)
    print('Get Info: ', data)
    if data:
        if b.check_password_hash(data['password'], request.form['password']):
            session['id'] = data['id']
            session['logged_in'] = True
            return redirect('/userDashboard/' + str(session['id']))

@app.route('/userDashboard/<user_id>')
def user_dashboard(user_id):#Get all recipes for display on table
    if 'logged_in' in session:
        if session['logged_in']:
            data = {'id' : user_id}
            User.login_user(data)
            return render_template('dashboard.html')
    return redirect('/')