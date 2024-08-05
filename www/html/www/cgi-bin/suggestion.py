#!/usr/bin/env python

import cgi
import json

# Get the query parameter from the URL
form = cgi.FieldStorage()
query = form.getvalue('q', '')

# Sample suggestions (you can replace it with your MongoDB query)
suggestions = ["ls", "ls -l", "cd", "mkdir", "touch", "rm", "mv", "cp", "pwd",
               "grep", "find", "cat", "echo", "chmod", "chown", "wget", "tar", "zip", "unzip"]

# Filter suggestions based on the query
filtered_suggestions = [s for s in suggestions if query in s]

# Output JSON response
print("Content-Type: application/json\n")
print(json.dumps(filtered_suggestions))

