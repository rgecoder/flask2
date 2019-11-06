from flask import Flask, session, request, redirect, render_template, flash

app = Flask(__name__)

app.secret_key = 'secretkey'


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def process():
    print(request.form['comment'])

    if len(request.form['comment'])< 1:
        flash("Comment field cannot be blank!")
        return redirect ('/')

    elif len(request.form['comment']) > 120:
        flash("Comment field should be no longer than 120 characters", "comment")
    
    if len(request.form['name']) < 1:
        flash("Name field cannot be blank!", "name")
        

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/success')


@app.route('/success')
def success():
    return render_template('result.html')


app.run(debug=True)
