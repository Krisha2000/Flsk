from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/n")
def details():
    a="Company Name: ABC Corporation"
    b="Location: India"
    c="Contact Detail: 999-999-9999"
    return a,b,c

if __name__ == '__main__':
   app.run(host="0.0.0.0")