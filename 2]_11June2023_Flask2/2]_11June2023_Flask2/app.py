from flask import Flask
from flask import request, jsonify, render_template
  
app = Flask(__name__)   

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/math", methods = ["POST"])
def math_operations():
    if (request.method == "POST"):
        op = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if op == "add":
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "subtract":
            r = num1 - num2
            result = "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "multiply":
            r = num1 * num2
            result = "The prod of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "divide":
            r = num1 / num2
            result = "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)

        return render_template("results.html", result = result)
    

@app.route("/postman_operation", methods = ["POST"])
def math_operations1():
    if (request.method == "POST"):
        op = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if op == "add":
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "subtract":
            r = num1 - num2
            result = "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "multiply":
            r = num1 * num2
            result = "The prod of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif op == "divide":
            r = num1 / num2
            result = "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)

        return jsonify(result)

        
if __name__ =='__main__':  
    app.run(debug = True)  