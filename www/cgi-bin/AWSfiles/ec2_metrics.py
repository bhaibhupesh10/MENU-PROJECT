#!/usr/bin/env python3

import cgi
import cgitb
import boto3
from datetime import datetime, timedelta

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/plain\n")

# Parse the form data
form = cgi.FieldStorage()
instance_id = form.getvalue("instanceId")
aws_access_key_id = form.getvalue("awsAccessKey")
aws_secret_access_key = form.getvalue("awsSecretKey")
region_name = form.getvalue("regionName")

# Specify the AWS credentials and region
cloudwatch = boto3.client(
    'cloudwatch',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Define the parameters for the metric you want to retrieve
namespace = 'AWS/EC2'  # Example namespace
metric_name = 'CPUUtilization'  # Example metric

# Define the time range for the metrics
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

# Call the get_metric_statistics method
response = cloudwatch.get_metric_statistics(
    Namespace=namespace,
    MetricName=metric_name,
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,  # Period in seconds (e.g., 300 seconds = 5 minutes)
    Statistics=['Average'],  # Type of statistics (e.g., Average, Sum, Maximum, Minimum, SampleCount)
    Unit='Percent'  # Unit of the metric
)

# Format and print the retrieved data points
for data_point in response['Datapoints']:
    print(f"Time: {data_point['Timestamp']}, Average: {data_point['Average']}")

