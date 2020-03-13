from flask import Flask
from Helloflask import app

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello Flask"
