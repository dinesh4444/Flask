from flask import Flask

### WSGI Application  is used to communicate between the web server and web application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to simple flask app"

## this decorator is used to route to index page 
@app.route('/index')
def index():
    return "This is the index page "


if __name__ == '__main__':
    app.run(debug=True)