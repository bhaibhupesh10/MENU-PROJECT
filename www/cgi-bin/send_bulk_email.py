#!/usr/bin/env python3

import cgi
import cgitb
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Enable CGI traceback for debugging
cgitb.enable()

print("Content-Type: application/json\n")

def send_email(to_email, subject, body, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(login, to_email, text)
        server.quit()
        return {"recipient": to_email, "status": "success"}
    except Exception as e:
        return {"recipient": to_email, "status": "failed", "error": str(e)}

def send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password):
    results = []
    for recipient in recipient_list:
        result = send_email(recipient, subject, body, smtp_server, smtp_port, login, password)
        results.append(result)
    return results

# Get the form data
form = cgi.FieldStorage()
subject = form.getvalue("subject")
body = form.getvalue("body")
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "aakarpawar7489@gmail.com"
password = "yhbc jymk iosz spjk"  # Be cautious with hardcoding passwords

# Retrieve and process the recipients
recipient_field = form.getvalue("recipients")
recipient_list = [email.strip() for email in recipient_field.split(',') if email.strip()]

# Send the emails
results = send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password)

# Output the result as JSON
print(json.dumps({"results": results}))

