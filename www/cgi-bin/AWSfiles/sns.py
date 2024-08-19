#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print('Content-Type: text/html')
print()
import boto3
import cgi

access_key = ' '
secret_key = ' '

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

sns_client = session.client('sns')

form = cgi.FieldStorage()
name=form.getvalue('name')

response = sns_client.create_topic(Name=name)
print("Topic ARN:", response['TopicArn'])
