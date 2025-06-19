from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required to use sessions

@app.route('/')
def index():
    # Start a new game if no number is stored
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('guess.html', message=None)

@app.route('/guess', methods=['POST'])
def guess():
    try:
        user_guess = int(request.form['guess'])
    except ValueError:
        return render_template('index.html', message="Please enter a valid number.")

    number = session.get('number')
    if user_guess < number:
        message = "Too low!"
    elif user_guess > number:
        message = "Too high!"
    else:
        message = f"Correct! The number was {number}. Starting a new game."
        session.pop('number')  # Reset game

    return render_template('guess.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)