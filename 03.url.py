### Building URL Dynamically
## Vriable Rules and url Building 

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

## Result checker
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks < 50:
        result ="fail"
    else:
        result = "sucess"
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)