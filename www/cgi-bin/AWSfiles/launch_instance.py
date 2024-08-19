#!/usr/bin/env python3

import cgi
import cgitb
import json
import boto3
from botocore.exceptions import ClientError

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
instance_type = form.getvalue('instanceType')
image_id = form.getvalue('imageId')
region_name = form.getvalue('regionName')

def launch_aws_instance(instance_type, image_id, region_name):
    aws_access_key = ' '
    aws_secret_key = ' '

    ec2 = boto3.client(
        'ec2',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )
    
    try:
        response = ec2.run_instances(
            InstanceType=instance_type,
            ImageId=image_id,
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        return {"success": True, "instance_id": instance_id}
    except ClientError as e:
        return {"success": False, "error": str(e)}

if instance_type and image_id and region_name:
    result = launch_aws_instance(instance_type, image_id, region_name)
else:
    result = {"success": False, "error": "Missing one or more required fields"}

print(json.dumps(result))

