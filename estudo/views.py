from estudo import app
from flask import render_template, render_template



@app.route('/')

def homepage():
    return render_template('index.html')

