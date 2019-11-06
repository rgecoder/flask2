from flask import Flask, render_template, redirect, session, flash,request
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['post'])
def process():
    if len(request.form['name']) < 1:
        # display validation errors
        flash("Name cannot be empty!")
    else:
        # display success message
        flash(f"Success! Your name is {request.form['name']}.")

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
