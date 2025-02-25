from flask import Flask, render_template, request

# object
app = Flask(__name__)

# define url to access home function
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/getdata', methods = ['post'])
def getdata():
    num1 = request.form['num1']
    num2 = request.form['num2']
    op = int(request.form['op'])
    res = 0
    if op ==1:
        res = int(num1) + int(num2)
        msg = "Addition is " + str(res)
    elif op ==2:
        res = int(num1) - int(num2)
        msg = "Substraction is " + str(res)
    elif op ==3:
        res = int(num1) / int(num2)
        msg = "Division  is " + str(res)
    elif op ==4:
        res = int(num1) * int(num2)
        msg = "Multiplication is " + str(res)

    return render_template("getdata.html", msg = msg)

# run the project
app.run(debug=True)