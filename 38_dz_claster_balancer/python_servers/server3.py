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
            <head><title>Server 3 (Weight 4)</title></head>
            <body>
                <h1>Server 3 - Weight 4</h1>
                <p>Port: 8003</p>
                <p>Hostname: {hostname}</p>
                <p>Requested path: {self.path}</p>
                <p>Host header: {self.headers.get('Host', 'Not set')}</p>
            </body>
        </html>
        """.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8003), SimpleHandler)
    print("Server 3 (Weight 4) running on port 8003")
    server.serve_forever()
