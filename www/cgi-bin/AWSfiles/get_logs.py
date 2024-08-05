#!/usr/bin/env python3

import cgi
import cgitb
import boto3

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/plain\n")

# Parse the form data
form = cgi.FieldStorage()
log_group_name = form.getvalue("logGroupName")
log_stream_name = form.getvalue("logStreamName")
aws_access_key_id = form.getvalue("awsAccessKey")
aws_secret_access_key = form.getvalue("awsSecretKey")
region_name = form.getvalue("regionName")

# Function to get logs
def get_logs(log_group_name, log_stream_name, region_name='', aws_access_key_id='', aws_secret_access_key=''):
    # Create a CloudWatch Logs client with explicit credentials
    client = boto3.client(
        'logs',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Get log events
    response = client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        startFromHead=True  # Set to False to get the latest logs first
    )

    # Format log events
    logs = []
    for event in response['events']:
        logs.append(str(event['timestamp']) + ' ' + event['message'])

    return '\n'.join(logs)

# Get logs and output as plain text
logs = get_logs(log_group_name, log_stream_name, region_name, aws_access_key_id, aws_secret_access_key)
print(logs)

