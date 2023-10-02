# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        sender_email = 'your_email@gmail.com'
        sender_password = 'your_email_password'
        receiver_email = 'recipient_email@gmail.com'  # Change to your email

        subject = 'Contact Form Submission'
        body = request.form['message'].strip()  # Remove leading/trailing whitespace

        if not body:
            flash('Message is required.', 'error')
            return redirect(url_for('index'))

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash('Email could not be sent. Please try again later.', 'error')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
