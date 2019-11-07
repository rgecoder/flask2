from flask import Flask

from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL('mydb')
#invoke the connectToMySQL function and pass it the name of the database we're using
#connectToMySQL returns an instance of MySQLConnection, which we will store in the variable
# 'mysql'
mysql = connectToMySQL('mydb')
# now we may invoke the query_db method

print("all the users", mysql.query_db("SELECT * FROM users;"))

if __name__ == "__main__":
  app.run(debug=True)