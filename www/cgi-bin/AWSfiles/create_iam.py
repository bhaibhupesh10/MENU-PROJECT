#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()

import boto3
import cgi

# Read the form data
form = cgi.FieldStorage()
name = form.getvalue("name")
action = form.getvalue("action")

# AWS credentials (ensure these are kept secure in a production environment)
access_key = ' '
secret_key = ' '

# Initialize a session using the specified credentials
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

iam_client = session.client('iam')

if action == "create":
    # Create IAM user
    try:
        response = iam_client.create_user(UserName=name)
        print(f"IAM user '{name}' created successfully!")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"Error: IAM user '{name}' already exists.")
    except Exception as e:
        print(f"Error creating IAM user: {e}")

elif action == "delete":
    # Delete IAM user
    try:
        response = iam_client.delete_user(UserName=name)
        print(f"IAM user '{name}' deleted successfully!")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"Error: IAM user '{name}' does not exist.")
    except Exception as e:
        print(f"Error deleting IAM user: {e}")

else:
    print("Invalid action specified. Please use 'create' or 'delete'.")

