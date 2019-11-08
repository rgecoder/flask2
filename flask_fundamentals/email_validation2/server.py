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
        print(new_email_id)  # prints the entire row of new insert
    return redirect('/')


app.run(debug=True)
