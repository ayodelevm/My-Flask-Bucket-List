from flask import Flask, render_template, request ,url_for
from datetime import datetime

app = Flask(__name__)


User  = []

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
