# demo_server.py
# Simulates sending a SecureSign encrypted bundle over HTTP
# Run: python demo_server.py
# Then open: http://localhost:9090

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# ── Replace this with an actual encrypted bundle from your app ──
# Go to SecureSign → Sign a document → Encrypt Signed Bundle
# → Copy JSON → paste here
ENCRYPTED_BUNDLE = {
    "encrypted": {
        "salt": "PASTE_SALT_FROM_SECURESIGN_HERE",
        "iv":   "PASTE_IV_FROM_SECURESIGN_HERE",
        "ciphertext": "PASTE_CIPHERTEXT_FROM_SECURESIGN_HERE",
        "tag":  "PASTE_TAG_FROM_SECURESIGN_HERE"
    },
    "algorithm": "RSA-PSS-SHA256 + AES-256-GCM",
    "note": "Decrypt with password to read the signed contract"
}

PLAIN_BUNDLE = {
    "document": "Pay Bob Rs 50000",
    "signature": "3a4f9c2b1d...(signature)...",
    "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjAN...\n-----END PUBLIC KEY-----",
    "signer": "Alice",
    "timestamp": "2026-06-10T10:00:00Z"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/plain':
            data = json.dumps(PLAIN_BUNDLE, indent=2).encode()
            label = "PLAIN"
        else:
            data = json.dumps(ENCRYPTED_BUNDLE, indent=2).encode()
            label = "ENCRYPTED"
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(data))
        self.end_headers()
        self.wfile.write(data)
        print(f"Served {label} bundle ({len(data)} bytes)")

    def log_message(self, *args):
        pass  # suppress default logging

print("Server running:")
print("  http://localhost:9090/plain     ← plain bundle")
print("  http://localhost:9090/          ← encrypted bundle")
HTTPServer(('localhost', 9090), Handler).serve_forever()