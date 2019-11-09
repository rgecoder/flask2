from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-copy9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
# mysql = connectToMySQL('login1')
# object called bcrypt made by invoking function Bcrypt with app as arg
bcrypt = Bcrypt(app)
app.secret_key = 'secretkey'

def debugHelp(message = ""):
  print("\n\n-----------------------", message, "---------------------------")
  print('REQUEST.FORM:', request.form)
  print('SESSION:', session)



@app.route('/')
def index():
    # if 'userid' not in session:
    #     session['userid'] = False
    # if 'first_name' not in session:
    #     session['first_name'] = None

    return render_template('index.html')


@app.route('/register', methods=['POST'])
def create_user():
    error = False
    mysql = connectToMySQL('login1')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
        "email": request.form['email'],
    }
    check = mysql.query_db(query, data)
    # print("check[0]:" , check[0])

    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['password_cf']) < 1:
        flash("All input fields are required!", "top")
        error = True
    elif not NAME_REGEX.match(request.form['first_name']):
            flash("First Name field cannot contain numbers", "firstname")
            error = True

    if len(request.form['first_name']) < 2:
            flash("Invalid name length", 'firstname')

    if not NAME_REGEX.match(request.form['last_name']):
            flash("Last name field cannot contain numbers", 'lastname')
            error = True

    if len(request.form['last_name']) < 2:
            flash("Invalid name length: last name", "lastname")

    if len(request.form['password']) < 8:
            flash("password must be more than 8 characters", 'password')
            error = True

    if check:
        if check[0]['email'] == request.form['email']:
                flash("Email has already been registered!", "email")
                error = True

    if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email format", 'email')
            error = True

    if request.form['password'] != request.form['password_cf']:
            flash("Passwords do not match!", 'password')
            error = True

    if error == True:
        return redirect("/")

    elif error == False:
        session.clear()

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)

        mysql = connectToMySQL('login1')
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password_hash': pw_hash,
        }
        new_user_id = mysql.query_db(query, data)
        flash("Registration Successful! Thank you for registering, you may now login in!", 'registration')

        session['id'] = new_user_id
        
        print("\n\n---------", new_user_id)
        session['logged_in'] = True
        
        mysql = connectToMySQL('login1')
        query = "SELECT * FROM users WHERE id = %(session_id)s"
        data = {
          'session_id':session['id']
        }
        user = mysql.query_db(query,data)
        session['first_name'] = user[0]['first_name']
        return redirect('/success')


@app.route('/success')
def success():
  debugHelp("SUCCESS ROUTE")
  if 'id' in session:
    mysql = connectToMySQL('login1')
    query = "SELECT * FROM users"
    all_users = mysql.query_db(query)
    return render_template('success.html', users=all_users)
  else:
    flash("You must log in first!", "login")
    return redirect('/')



@app.route('/login', methods=['POST'])
def login():

    mysql = connectToMySQL('login1')
    query = 'SELECT * FROM users WHERE email = %(email)s;'
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)
    print(result)  # [ {} {} {} ] a list of dictionaries

    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['id'] = result[0]['id']
            session['first_name'] = result[0]['first_name']
            print(session['id'])

            return redirect('/success')
    else:
      flash("You could not be logged in!", "login")
      return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
  session.clear()
  debugHelp("LOGOUT ROUTE")
  return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
