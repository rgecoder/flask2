from flask import Flask, session, request, redirect, render_template, flash
import re


# import the function connectToMySQL from the file
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'secretkey'

# returns an instance of connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# fetching records
@app.route('/')
def index():
    # this must be inside the create route not at top
    mysql = connectToMySQL('emails')
    all_emails = mysql.query_db("SELECT * FROM emails")
    print("Fetched all emails", all_emails)

    return render_template('index.html', emails=all_emails)


# inserting records
@app.route('/create', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email!")
    else:

        mysql = connectToMySQL('emails')
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        data = {
            'email': request.form['email']

        }

        new_email_id = mysql.query_db(query, data)
        session['id'] = new_email_id
        
        print(new_email_id)
        print(session['id'])  # prints the entire row of new insert

        
    return redirect('/success')

@app.route('/success')
def results():
  mysql = connectToMySQL('emails')
  all_emails = mysql.query_db("SELECT * FROM emails")

  return render_template("results.html", emails = all_emails)

@app.route('/delete', methods=['POST'])
def delete():
  mysql = connectToMySQL('emails')
  id = int(request.form['hidden'])
  print(id)
  query = "DELETE FROM emails WHERE id = '{}';".format(id)
  
  print(session['id'])
  mysql.query_db(query)
  return redirect('/success')


app.run(debug=True)
