#!/usr/bin/env python3

import cgi
import cgitb
import paramiko
import json

# Enable CGI error reporting
cgitb.enable()

def ssh_connect(hostname, port, username, password):
    """Establish an SSH connection to the server."""
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        
        # Automatically add the server's host key (not recommended for production)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(hostname, port, username, password)
        return ssh_client
    except Exception as e:
        return None, str(e)

def execute_command(ssh_client, command):
    """Execute a command on the remote server via SSH."""
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        if output:
            return output.strip()
        if error:
            return error.strip()
        return ""
    except Exception as e:
        return str(e)

# Print the Content-Type header required for CGI responses
print("Content-Type: application/json\n")

# Parse form data
form = cgi.FieldStorage()

# Get form data
hostname = form.getvalue('hostname')
port = int(form.getvalue('port', 22))
username = form.getvalue('username')
password = form.getvalue('password')
command = form.getvalue('command')

# Response dictionary
response = {}

if not all([hostname, username, password, command]):
    response['error'] = 'All fields are required.'
else:
    # Establish SSH connection
    ssh_client, error_msg = ssh_connect(hostname, port, username, password)
    if ssh_client:
        # Execute command
        result = execute_command(ssh_client, command)
        response['output'] = result
        ssh_client.close()  # Close SSH connection
    else:
        response['error'] = f'Failed to connect to {hostname}:{port}. Error: {error_msg}'

# Output the result as JSON
print(json.dumps(response))

