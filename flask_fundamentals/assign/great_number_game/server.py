from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
  if 'number' not in session:
    session['number'] = random.randrange(0,101)
    session['button'] = 'submit'
  print (session['number'])

  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
  if int(request.form['guess']) > int(session['number']):
    session['comment'] = "Too High!"
    session['color'] = 'red'
  elif int(request.form['guess']) < int(session['number']):
    session['comment'] = "Too Low!"
    session['color'] = 'red'
  else: 
    session['comment'] = request.form['guess'] + " was the number!"
    session['button'] = 'Play Again!'
    session['color'] = 'green'
    

  
  return redirect('/')




app.run(debug=True)