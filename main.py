import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

class PHPMailer:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, to_address, subject, message):
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.username, self.password)

            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_address
            msg['Subject'] = subject

            body = message
            msg.attach(MIMEText(body, 'plain'))

            server.send_message(msg)
            del msg
            server.quit()

            print('Email sent successfully!!')
        except Exception as e:
            print('Error', str(e))

def main():
    smtp_server = "smtp.gmail.com"
    port = 587
    username = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    if not username or not password:
        print("Email credentials are not set in environment variables.")
        return

    mailer = PHPMailer(smtp_server, port, username, password)

    while True:
        mailer.send_email('email@email.com', 'subject', 'body!')
        time.sleep(2)

if __name__ == "__main__":
    main()
