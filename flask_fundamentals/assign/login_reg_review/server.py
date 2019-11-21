from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-copy9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)

bcrypt = Bcrypt(app)
app.secret_key='secretkey'

def debugHelp(message = ""):
  print("\n\n------------", message, "--------------")
  print('REQUEST.FORM:', request.form)
  print('SESSION:', session)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register',methods=['POST'])
def create_user():
  error = False
   mysql = connectToMySQL('login1')
   query = "SELECT * FROM users WHERE email = %(email)s;"
   data = {
     "email": request.form['email'],
   }

   check = mysql.query_db(query,data)
   