#!/usr/bin/env python3

import boto3
import cgi
import cgitb
import json

# Enable CGI traceback for debugging
cgitb.enable()

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Parse form data
form = cgi.FieldStorage()

# Get action from form data
action = form.getvalue('action')
table_name = form.getvalue('table_name')

def list_tables():
    response = dynamodb.list_tables()
    return response['TableNames']

def create_table(table_name):
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return response

def delete_table(table_name):
    response = dynamodb.delete_table(TableName=table_name)
    return response

def put_item(table_name, item):
    response = dynamodb.put_item(TableName=table_name, Item=item)
    return response

def get_item(table_name, key):
    response = dynamodb.get_item(TableName=table_name, Key=key)
    return response.get('Item')

def delete_item(table_name, key):
    response = dynamodb.delete_item(TableName=table_name, Key=key)
    return response

# Route the action
if action == 'list_tables':
    result = list_tables()
elif action == 'create_table':
    result = create_table(table_name)
elif action == 'delete_table':
    result = delete_table(table_name)
elif action == 'put_item':
    item = json.loads(form.getvalue('item'))
    result = put_item(table_name, item)
elif action == 'get_item':
    key = json.loads(form.getvalue('key'))
    result = get_item(table_name, key)
elif action == 'delete_item':
    key = json.loads(form.getvalue('key'))
    result = delete_item(table_name, key)
else:
    result = {'error': 'Invalid action'}

# Output the result as JSON
print("Content-Type: application/json")
print()
print(json.dumps(result, indent=4))

