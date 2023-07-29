import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, name, email, subject, message):
        self.user_message = message
        self.name = name
        self.email = email
        # <--------------------Sender's Credentials---------------------------->
        f = open(file="config.json")
        creds = json.load(f)
        self.my_email = creds["email"]
        self.my_password = creds["app_password"]
        self.subject = subject

    def send_email(self):
        self.to_email = "shahaagam04@gmail.com"
        self.message = MIMEMultipart('mixed')
        self.message['Subject'] = self.subject
        self.message['From'] = self.my_email
        self.message['To'] = self.to_email

        # Create the body of the message
        msg = f"""
Name: {self.name}

Email: {self.email}

Message: {self.user_message}
"""
        self.message.attach(MIMEText(msg, 'plain'))

        with smtplib.SMTP(host="smtp.gmail.com", port=587, local_hostname="localhost") as self.connection:
            self.connection.starttls()
            self.connection.login(user=self.my_email, password=self.my_password)
            self.connection.sendmail(from_addr=self.my_email, to_addrs=self.to_email, msg=self.message.as_string())