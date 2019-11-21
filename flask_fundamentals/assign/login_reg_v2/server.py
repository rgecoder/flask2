import re
from flask import Flask, session, request, redirect, flash, render_template
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secretkey"

# Login page
@app.route('/')
def index():
  return render_template('login.html')

#login route process the login form
@app.route('/login', methods=['GET','POST'])
def login():
  
  #database named 'login2'
  #get the user data from the db based on the email provided in form
  mysql = connectToMySQL('login2')
  query = "SELECT * from users where email = %(email)s;"
  data = {
    'email':request.form['email']
  }
  get_user = mysql.query_db(query,data)

  if get_user:
    session['userid'] = get_user[0]['id']
    session['first_name'] = get_user[0]['first_name']
    hashed_password = get_user[0]['password']
    if bcrypt.check_password_hash(hashed_password, request.form['password']):
      session['logged_in'] = True
      flash("You have succesfully logged in!", "login")
      return redirect('/homepage')
    else:
      session['logged_in'] = False
      flash("Login failed!",'login')
      return redirect('/')
  else:
    flash("Email not found, please register!", 'login')
    return redirect ('/')

#home page logout
@app.route('/logout', methods=['GET'], ['POST'])
def logout():
  session['logged_in'] = False
  flash("You have been logged out!", 'login')
  return redirect ('/')

#registration page
@app.route('/register', methods=['GET','POST']
def register():
  error = 0
  if request.method == 'POST':
    #check first name (2 chars, submitted, and letters only)
    first_name = request.form['first_name']
    if not first_name:
      error += 1
      flash




