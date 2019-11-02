from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", x=4)



@app.route('/<x>/<y>')
def checker(x,y):
  return render_template("index.html", x=int(x)/2, y=int(y)/2)


app.run(debug=True)

