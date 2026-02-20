from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    num3 = int(num1) + int(num2)
    return str(num3)

@app.route("/sub/<int:num1>/<int:num2>")
def sub(num1, num2):
    num3 = int(num1) - int(num2)
    return str(num3)


@app.route("/login/<username>/<password>")
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    return "Login failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True) #localhost:8001