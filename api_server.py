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


# Defining class for request handling to server

# Deliberate defined a custom method (not adhering to any API standards)

class APIRequestHandling(BaseHTTPRequestHandler):
    def do_RETRIEVE(self):
        if self.path == '/hello/name':
            self.send_response(200, message='OK!')
            self.send_header('XYZ', 'Define your header here')
            self.end_headers()
            message = {'Name' : 'Shek'}
            self.wfile.write(json.dumps(message).encode('utf-8'))
        else:
            self.send_response(404, message='Not Found!')
            self.end_headers()
            message = {'File' : 'Not Found!'}
            self.wfile.write(json.dumps(message).encode('utf-8'))
            self.log_error('Requested path does not exist')

# For a POST request, you read the length of the incoming stream of data (payload data) using Content-Length header. 
# The incoming stream of payload data is sent separately from the header. The Content-Length header lets the server know of the payload data size.
# The Content-Type Header will also let the server know of the type of data being received.
# It is important that you explicitly define these headers. 

    def do_POST(self):
        if self.path == '/posty':
            content_length = int(self.headers['Content-Length'])
            payload_data = self.rfile.read(content_length)
            check_length = {'length-of-body': content_length, 'data': payload_data}
            decoded_json_data = json.loads(payload_data)
            reason = decoded_json_data.get('Reason')
            self.send_header('Location', 'Melbourne')
            self.end_headers()
            self.send_response(200, message='OK')
            self.wfile.write(payload_data)
            self.wfile.write(json.dumps(check_length).encode('utf-8'))

            with open('payload_write.txt', mode='a') as f:
                f.write(json.dumps(decoded_json_data))

        else:
            self.send_response(404)
            self.end_headers()
            message = {'Error': 'Invalid Endpoint, Not found!'}
            self.wfile.write(json.dumps(message).encode('utf-8'))
            
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, APIRequestHandling)
    print("Starting Server...It's a simple HTTP Server :-)")
    print("Query the API using the methods defined")
    httpd.serve_forever()

if __name__ == '__main__':
    run();
