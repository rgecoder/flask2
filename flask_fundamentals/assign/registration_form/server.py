from flask import Flask, request, redirect, session, render_template, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")

    elif not EMAIL_REGEX.match(request.form['email']):
        print(EMAIL_REGEX.match(request.form['email'])) 
        #gives none if not matching
        flash("Invalid Email Address!")

    if len(request.form['first_name']) < 1:
      flash("First name cannot be blank!")

    if len(request.form['last_name']) < 1:
      flash("Last name cannot be blank!")
    
    if len(request.form['password']) < 1:
      flash("Password cannot be blank!")

    elif len(request.form['password']) < 8:
      flash("Password must be more than 8 characters")
    
    elif request.form['password'] != request.form['conf_password']:
      flash("Passwords do not match!")

    
    if '_flashes' in session.keys():
      return redirect('/')
        
    
    else:
      session['first_name'] = request.form['first_name']
      session['last_name'] = request.form['last_name']
      session['email'] = request.form['email']
      session['password'] = request.form['password']

      return redirect('/success')

@app.route('/success')
def success():
  return render_template('success.html')


app.run(debug=True)
