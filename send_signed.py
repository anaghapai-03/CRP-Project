# send_signed.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# This simulates sending a SecureSign encrypted bundle
# (copy an actual encrypted bundle JSON from your app)
ENCRYPTED_BUNDLE = json.dumps({
    "encrypted": {
        "salt": "a3f9b2c1d4e5f6a7b8c9d0e1f2a3b4c5",
        "iv": "1a2b3c4d5e6f7a8b9c0d1e2f",
        "ciphertext": "8f3a9b2c1d4e5f6789abcdef0123456789abcdef...",
        "tag": "abcdef0123456789abcdef0123456789"
    },
    "algorithm": "RSA-PSS-SHA256 + AES-256-GCM"
})

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(ENCRYPTED_BUNDLE.encode())
    def log_message(self, *args): pass

print("Server running on http://localhost:9090")
HTTPServer(('localhost', 9090), Handler).serve_forever()