from flask import Flask, render_template, request
import os
import json
from datetime import datetime

app = Flask(__name__)
LETTERS_DIR = 'letters'

if not os.path.exists(LETTERS_DIR):
    os.makedirs(LETTERS_DIR)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        send_date = request.form['date']
        email = request.form['email']

        filename = f"{LETTERS_DIR}/{datetime.now().timestamp()}.json"
        with open(filename, 'w') as f:
            json.dump({
                'email': email,
                'message': message,
                'send_date': send_date
            }, f)

        return "✅ Letter saved! It will be emailed to you on your selected date."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
