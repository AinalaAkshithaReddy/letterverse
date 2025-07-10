import os
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

LETTERS_DIR = 'letters'

# 🔒 Replace with your actual Gmail
SMTP_USER = 'letterverse.future@gmail.com'  # your email
SMTP_PASS = 'qtrbymrayuvssldt'    # app password (not your email password!)

def send_email(to, content):
    msg = MIMEText(content)
    msg['Subject'] = '📬 A Letter from Your Past Self'
    msg['From'] = SMTP_USER
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

def process_letters():
    for filename in os.listdir(LETTERS_DIR):
        filepath = os.path.join(LETTERS_DIR, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)

        send_date = datetime.strptime(data['send_date'], "%Y-%m-%d").date()

        # If the send date is today or before, send the letter
        if send_date <= datetime.today().date():
            send_email(data['email'], data['message'])
            os.remove(filepath)
            print(f"✅ Sent letter to {data['email']}")

if __name__ == '__main__':
    process_letters()
