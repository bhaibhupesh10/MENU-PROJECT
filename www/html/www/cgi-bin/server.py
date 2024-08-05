import http.server
import socketserver
import os

PORT = 8000

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']

# Change the current working directory to your website directory
os.chdir('/path/to/your/website')

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()

