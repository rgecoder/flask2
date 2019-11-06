from flask import Flask, request, redirect, session, flash, render_template
import re
app = Flask(__name__)
app.secret_key = 'secretkey'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods = ['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!")
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid Email Address!")
  
  if len(request.form['name']) < 1:
    flash("Name cannot be blank!")
  elif len(request.form['name']) <= 3:
    flash("Name must be 3+ characters", "name")
  
  if len(request.form['comment'])<1:
    flash("comment cannot be blank!", "comment")
  elif len(request.form['comment']) > 100:
    flash("coment must be less than 100 char", "comment")

  if '_flashes' in session.keys():
    return redirect('/') 
  else:
    return redirect('/success')

app.run(debug=True)

