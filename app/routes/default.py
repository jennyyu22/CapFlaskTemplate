from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/quizpage')
def quizpage():
    return render_template('quizpage.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/results')
def results():
    return render_template('results.html') 
