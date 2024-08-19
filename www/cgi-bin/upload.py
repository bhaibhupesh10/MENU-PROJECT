#!/usr/bin/python3
import cgi
import os
import time
upload_dir = "myupload/"

print("Content-Type: text/plain")
print()

try:
    form = cgi.FieldStorage()
    image_file = form['image']
    
    if image_file.filename:
        timestamp = int(time.time())
        filename = f"image_{timestamp}.png"
        
        filepath = os.path.join(upload_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(image_file.file.read())
        print("Image uploaded successfully")
    else:
        print("No image file received")
except Exception as e:
    print("An error occurred:", str(e))

