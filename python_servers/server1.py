#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"""
        <html>
            <head><title>Server 1</title></head>
            <body>
                <h1>Server 1 (Port 8001)</h1>
                <p>Hostname: {hostname}</p>
                <p>Requested path: {self.path}</p>
            </body>
        </html>
        """.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8001), SimpleHandler)
    print("Server 1 running on port 8001")
    server.serve_forever()
