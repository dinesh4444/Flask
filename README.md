# FLASK

* Web application framework
* Written in python
* Used for End-to-end project

- Developed by Armin Ronacher he leads a python programmer group name poco
- Flask framework based on WSGI(Web service Gateway Interfce) & Jinja2 template engine

To install flask 
---
!pip install flask
---

### Basic Flask app 

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

# Building URL Dynamically
Here is an example of how to build a URL Dynamically using the following syntax:

---
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "This is first page"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "<html><body><h1>The person has passed and score the marks</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and score the marks is " + str(score)

* Result checker
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks < 50:
        result ="fail"
    else:
        result = "sucess"
    return redirect(url_for(result, score=marks))

---

redirect = is to redirect to the perticular url with a trailing slash with a url_for(page, rule) parameter

# Integrate HTML with Flask
Create a templates folder in current directory and make index.html, and pages you want to add 
to the application

---
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>index</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>
        <h2>HTML Forms</h2>

        <form action="/submit" method='post'>
            <label for="Science">Science:</label><br>
            <input type="text" id='science' name="science" value=0><br>
            <label for="Maths">Maths:</label><br>
            <input type="text" id='maths' name="maths" value=0><br>
            <label for="C">C:</label><br>
            <input type="text" id='c' name="c" value=0><br>
            <label for="datascience">Data Science:</label><br>
            <input type="text" id='datascience' name="datascience" value=0><br>
            <input type="submit" value="Submit">
        </form>

        <p>If you click the "Submit" button, the form data will be sent to the page called "/submit"</p>       
        
        <script src="" async defer></script>
    </body>
</html>

---

# Jinja2 

---
{% if result>= 50 %}
<h1>Your Result is Passed</h1>
{% else %}
<h1>Your result is failde</h1>
{% endif %}
---

# webcam index.html
---
<html>
    <body>
        <h1>Live streaming</h1>
        <div>
            <img src="{{ url_for('video') }}" width="50%">
        </div>
    </body>
</html>
---

# Live camera straming code

---
def generate_frames():
    while True:
        ## Read the camera frame
        sucess, frame = cam.read()
        if not sucess:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

---




