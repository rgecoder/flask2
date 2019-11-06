from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order_info = {
        'strawberry':request.form['strawberry'],
        'raspberry':request.form['raspberry'],
        'apple': request.form['apple'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'student_id': request.form['student_id'],
    }
    print(request.form)
    print(int(order_info['strawberry']) + int(order_info['raspberry']))
    return render_template("checkout.html", orders=order_info)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    