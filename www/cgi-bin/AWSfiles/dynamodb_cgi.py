#!/usr/bin/env python3

import boto3
import cgi
import cgitb
import json

# Enable CGI traceback for debugging
cgitb.enable()

# AWS credentials (Please replace with your actual credentials)
AWS_ACCESS_KEY_ID = ' '
AWS_SECRET_ACCESS_KEY = ' '
AWS_REGION = 'ap-south-1'

# Create a DynamoDB client
dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Parse form data
form = cgi.FieldStorage()
action = form.getvalue('action')

def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=json.loads(key_schema),
            AttributeDefinitions=json.loads(attribute_definitions),
            ProvisionedThroughput=json.loads(provisioned_throughput)
        )
        return response
    except Exception as e:
        return {'error': str(e)}

def list_tables():
    try:
        response = dynamodb.list_tables()
        return response
    except Exception as e:
        return {'error': str(e)}

def delete_table(table_name):
    try:
        response = dynamodb.delete_table(TableName=table_name)
        return response
    except Exception as e:
        return {'error': str(e)}

# Handle the action
response = {}
if action == 'create_table':
    table_name = form.getvalue('table_name')
    key_schema = form.getvalue('key_schema')
    attribute_definitions = form.getvalue('attribute_definitions')
    provisioned_throughput = form.getvalue('provisioned_throughput')
    response = create_table(table_name, key_schema, attribute_definitions, provisioned_throughput)
elif action == 'list_tables':
    response = list_tables()
elif action == 'delete_table':
    table_name = form.getvalue('table_name')
    response = delete_table(table_name)
else:
    response = {'error': 'Invalid action'}

# Output the response as JSON
print("Content-Type: application/json")
print()
print(json.dumps(response))

