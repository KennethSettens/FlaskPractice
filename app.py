from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 

app = Flask(__name__)
debug = DebugToolbarExtension(app)
app.config['SECRET_KEY'] = "purp"

responses = []

@app.route('/')
def index():
    return render_template('home.html')