from flask import Flask, request, redirect, session, flash, render_template
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')

from mysqlconnection import connectToMySQL

app=Flask(__name__)

mysql = connectToMySQL('emails')
app.secret_key=('secretkey')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  query = "SELECT * FROM emails WHERE email = %(email)s;"
  data = {'email' : request.form['email']}
  result = mysql.query_db(query,data)
  
  
  if len(request.form['email']) < 1:
    flash("Email cannot be blank!")

  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid email address!")

  else:
    if result:
      flash("Email already in database!")
    else:
      # query = "INSERT INTO emails (email, created_at) VALUE(%(email)s, NOW())"
      # data = {"email": request.form['email']}

      # new_user_id = mysql.query_db(query,data)

      # return redirect('/results')
      email= request.form['email']
      session['email'] = email
      query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW())"
      data = {"email": request.form['email']}
      print(query)
      mysql.query_db(query, data)

  return redirect('/results')

  @app.route('/results')
  def show():
    query = "SELECT * FROM emails"
    emailList = mysql.fetch(query)
    return render_template('results.html', email=session['email'], list=emailList)


app.run(debug=True)

  