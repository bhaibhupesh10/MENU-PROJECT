#!/usr/bin/env python3
import cgi
import os

# Enable debugging
import cgitb
cgitb.enable()

# Set content type
print("Content-Type: text/html\n")

# Parse form data
form = cgi.FieldStorage()

# Check if image data was uploaded
if "image" in form:
    # Get the uploaded image data
    image_data = form["image"].file.read()

    # Write the image data to a file
    with open("/var/www/html/uploaded_image.jpg", "wb") as f:
        f.write(image_data)

    # Display uploaded image
    print("<html><body>")
    print("<h1>Uploaded Image</h1>")
    print('<img src="/uploaded_image.jpg" alt="Uploaded Image">')
    print("</body></html>")
else:
    print("<html><body>")
    print("<h1>Error: No image uploaded!</h1>")
    print("</body></html>")

