from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-copy9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
  debugHelp("INDEX METHOD")
  return render_template("index.html")

@app.route('/reserve', methods=['POST'])
def reserve():
  #let's add validations here
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!", 'email')
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid Email Address!", 'email')
  
  if len(request.form['name']) < 1:
    flash("Name cannot be blank!", 'name')
  elif len(request.form['name']) <=3:
    flash("Name must be 3+ characters", 'name')
  
  if len(request.form['pin']) < 1:
    flash("Pin cannot be blank!", 'pin')
  elif request.form['pin'].isdigit() == False:
    flash("Pin must be numeric", 'pin')
  elif len(request.form['pin']) < 4 or len(request.form['pin']) > 8:
    flash("Pin must be 4-8 digits", 'pin')


  debugHelp("RESERVE METHOD")
  if '_flashes' in session.keys():
    return redirect ('/')
  else:
    session['name'] = request.form['name']
    return redirect ('/success')

@app.route('/success')
def success():
  return "Thank you " + session['name'] + ", your seat is now reserved!"

def debugHelp(message = ""):
  print("\n\n-----------------------", message, "--------------------")
  print('REQUEST.FORM:', request.form)
  print('SESSION', session)


if __name__ == "__main__":
  app.run(debug=True)