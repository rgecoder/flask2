from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  users = {'name':request.form['name'], 
          'location':request.form['location'],
          'comment':request.form['comment'],
          }

 
  return render_template('/result.html', users = users)



if __name__ == "__main__":
  app.run(debug=True)