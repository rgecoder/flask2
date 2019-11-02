from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  users= (
    {'first_name':'Michael', 'last_name':'Choi'},
    {'first_name':'John', 'last_name':'Tan'},
    {'first_name':'Mark', 'last_name':'Wells'},
    {'first_name':'Kevin', 'last_name':'Bacon'}
  );

  return render_template("index.html", users = users)

app.run(debug=True)