from http.server import SimpleHTTPRequestHandler
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
