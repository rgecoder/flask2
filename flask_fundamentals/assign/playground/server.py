from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", times=3)

@app.route('/play/<times>')
def play(times):
  return render_template("index.html", times=int(times))

@app.route('/play/<times>/<color>')
def playcolor(times, color):
  return render_template("index.html", times=int(times), color=color)


app.run(debug=True)