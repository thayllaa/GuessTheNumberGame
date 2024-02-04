from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def generate_secret_number():
    return random.randrange(1, 101)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        level = int(request.form['level'])
        total_tries = 0

        if level == 1:
            total_tries = 20
        elif level == 2:
            total_tries = 10
        elif level == 3:
            total_tries = 5

        secret_number = generate_secret_number()
        return render_template('game.html', total_tries=total_tries, secret_number=secret_number, tries_left=total_tries)

    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    chosen_number = int(request.form['chosen_number'])
    secret_number = int(request.form['secret_number'])
    tries_left = int(request.form['tries_left']) - 1

    if chosen_number == secret_number:
        result = "Congratulations! You guessed the secret number."
        return render_template('result.html', result=result)
    elif tries_left == 0:
        return render_template('game_over.html', secret_number=secret_number)
    else:
        result = "Your guess is "
        if chosen_number > secret_number:
            result += "higher than the secret number."
        else:
            result += "lower than the secret number."
        return render_template('game.html', tries_left=tries_left, secret_number=secret_number, result=result)

if __name__ == '__main__':
    app.run(debug=True)
