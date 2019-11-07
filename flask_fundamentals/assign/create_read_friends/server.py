from flask import Flask, render_template,request, redirect

from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL('mydb')

@app.route('/')
def index():
  mysql = connectToMySQL("friends")
  all_friends = mysql.query_db("SELECT * FROM friends")
  print ("Fetched all friends", all_friends)

  return render_template("index.html", friends = all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
  mysql = connectToMySQL("friends")
  query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"

  data = {
        'first_name':request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
  }

  new_friend_id = mysql.query_db(query,data)

  return redirect('/')


app.run(debug=True)