#!/usr/bin/env python

# You may have to use python3 instead of python, I've locally aliased python3.11 to be python.

# Going to implement a basic HTTP server over here using the ```http.server module```
# Ref https://docs.python.org/3/library/http.server.html

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# What do I need to do?
# Start server on port 8080.
# Send request to port 8080
# Receive response

# How do I start server on port 8080?
# I need to make port 8080 listen for HTTP traffic.


# Defining class for request handling to server

class APIRequestHandling(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200, message='OK!')
            self.send_header('Location', 'Melbourne')
            self.end_headers()
            message = {'Name' : 'Abhisheks web server'}
            self.wfile.write(json.dumps(message).encode())
        else:
            self.send_response(404, message='Not Found!')
            self.end_headers()
            message = {'File' : 'Not Found!'}
            self.wfile.write(json.dumps(message).encode())
            self.log_error('Requested path does not exist')


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, APIRequestHandling)
    print("Starting Server...")
    httpd.serve_forever()

if __name__ == '__main__':
    run();
