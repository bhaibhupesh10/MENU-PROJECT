#!/usr/bin/env python3

import cgi
import cgitb
from twilio.rest import Client

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
to_number = form.getvalue('to_number')
message_body = form.getvalue('message')

def send_sms_message(to_number, message_body):
    account_sid = 'AC663bbeae958020fdb964880572b351ea'
    auth_token = '216637c796472c70ce42cf60eb2db441'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_='+14127752408',
        to=to_number
    )
    return "SMS sent successfully."

if to_number and message_body:
    result = send_sms_message(to_number, message_body)
else:
    result = "Missing to_number or message."

print(f"<html><body><h1>{result}</h1></body></html>")

