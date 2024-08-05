#!/usr/bin/env python3

import boto3
import json
import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

def get_logs(log_group_name, log_stream_name, region_name):
    try:
        client = boto3.client(
            'logs',
            region_name=region_name,
            aws_access_key_id='AKIA2UC3BHYJSUOHZZSG',
            aws_secret_access_key='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'
        )
        
        # Get log events
        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startFromHead=True  # Set to False to get the latest logs first
        )

        # Prepare log events for JSON output
        log_events = [{'timestamp': event['timestamp'], 'message': event['message']} for event in response['events']]
        
        # Return JSON response
        print("Content-Type: application/json\n")
        print(json.dumps(log_events))

    except client.exceptions.ResourceNotFoundException as e:
        print("Content-Type: application/json\n")
        print(json.dumps({'error': f"Resource not found: {e}"}))
    except Exception as e:
        print("Content-Type: application/json\n")
        print(json.dumps({'error': f"An error occurred: {e}"}))

# Main CGI script logic
if __name__ == "__main__":
    form = cgi.FieldStorage()
    log_group_name = form.getvalue('log_group_name', '/aws/lambda/lamdafun1')
    log_stream_name = form.getvalue('log_stream_name', '2024/06/24/[$LATEST]a9cb10a289884d55a33391431d7fa6cd')
    region_name = form.getvalue('region_name', 'ap-south-1')
    
    # Call function to fetch and print logs
    get_logs(log_group_name, log_stream_name, region_name)

