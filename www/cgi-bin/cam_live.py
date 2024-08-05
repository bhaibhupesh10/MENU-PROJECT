#!/usr/bin/env python3

import cgi
import cgitb

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html\n")

# Print the HTML content
with open("cam_live.html", "r") as f:
    print(f.read())

