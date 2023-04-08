# FLASK

* Web application framework
* Written in python
* Used for End-to-end project

- Developed by Armin Ronacher he leads a python programmer group name poco
- Flask framework based on WSGI(Web service Gateway Interfce) & Jinja2 template engine

To install flask 
---
pip install flask
---

* Basic Flask app 

---
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"


if __name__ == '__main__':
    app.run(debug=True)

---

* this flask app is running on http://127.0.0.1:5000/  this port 



