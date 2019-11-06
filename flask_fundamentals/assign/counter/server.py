from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
  if 'count' in session:
    session['count'] += 1
  else:
    session['count'] = 0

  return render_template('index.html') 

@app.route('/destroy_session')
def destroy():
  session.clear()
  return redirect ('/')



app.run(debug=True)