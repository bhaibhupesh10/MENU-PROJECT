#!/usr/bin/python3
import boto3
import cgi
import os
import sys

print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print('Content-Type: text/html')
print()

# AWS credentials (ensure these are kept secure in a production environment)
access_key = 'AKIA2UC3BHYJSUOHZZSG'
secret_key = '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'

# Initialize a session using the specified credentials
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

# Initialize S3 and SES clients
s3_client = session.client('s3')
ses_client = session.client('ses')

form = cgi.FieldStorage()
action = form.getvalue('action')

def list_buckets():
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets

def create_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_email_list():
    bucket = form.getvalue('bucket_name')
    user_subject = form.getvalue('subject')
    user_message = form.getvalue('message')
    source_email = form.getvalue('source_email')

    # Get the uploaded file
    fileitem = form['file']
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        open('/tmp/' + fn, 'wb').write(fileitem.file.read())

        # Upload the file to the selected S3 bucket
        with open('/tmp/' + fn, 'rb') as f:
            s3_client.upload_fileobj(f, bucket, fn)
        
        # Retrieve the email list from S3
        data = s3_client.get_object(Bucket=bucket, Key=fn)
        emailstr = data["Body"].read().decode('utf-8')
        emaillist = emailstr.split(",")

        # Send the email using SES
        try:
            res = ses_client.send_email(
                Source=source_email,
                Destination={
                    'ToAddresses': emaillist,
                },
                Message={
                    'Subject': {
                        'Data': user_subject,
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Text': {
                            'Data': user_message,
                            'Charset': 'UTF-8'
                        },
                    }
                }
            )
            print(f"Email sent successfully: {res}")
        except Exception as e:
            print(f"Error sending email: {e}")
    else:
        print("No file was uploaded")

if action == 'list_buckets':
    buckets = list_buckets()
    print(','.join(buckets))
elif action == 'create_bucket':
    bucket_name = form.getvalue('bucket_name')
    create_bucket(bucket_name)
elif action == 'upload_email_list':
    upload_email_list()
else:
    print("Invalid action")

