from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", x=4, y=4)

@app.route('/<x>/<y>')
def checker(x,y):
  return render_template("index.html", x = int(x), y=int(y))

app.run(debug=True)