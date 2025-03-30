import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from os import getenv

host = "smtp.gmail.com"
port = 465
password = os.getenv("PASSWORD")
username = "neerajshimpi2912@gmail.com"
context = ssl.create_default_context()
receiver = "neerajshimpi2912@gmail.com"

def sendmail(user_email_local, message_local):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = receiver
        msg["Subject"] = "New Contact Me Form Submission"
        email_body = f"User Email: {user_email_local}\n\nMessage:\n{message_local}"
        msg.attach(MIMEText(email_body, "plain"))
        server.sendmail(username, receiver,msg.as_string())