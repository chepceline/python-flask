from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

if _name_ == '_main_':
    app.run(debug == True)    