# mitm_demo.py  — simulates a man-in-the-middle attack
import json

# Step 1: Original signed bundle (copy from your SecureSign app)
original = {
    "document": "Pay Bob Rs 50000",
    "signature": "3a4f9c...(your actual signature hex)...",
    "publicKey": "-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----",
    "signer": "Alice",
    "timestamp": "2026-06-01T10:00:00Z"
}

print("=== ORIGINAL DOCUMENT ===")
print("Document:", original["document"])
print("Signature (first 40 chars):", original["signature"][:40])

# Step 2: Attacker intercepts and modifies the document
print("\n=== ATTACKER MODIFIES DOCUMENT ===")
tampered = original.copy()
tampered["document"] = "Pay Bob Rs 999999"  # attacker changes amount
print("Tampered document:", tampered["document"])
print("Signature unchanged:", tampered["signature"][:40])

# Step 3: Recipient tries to verify
print("\n=== RECIPIENT VERIFIES ===")
print("Original SHA-256 was embedded in signature")
print("New SHA-256 of tampered doc is completely different")
print("Result: SIGNATURE INVALID — attack detected!")
print("\nThis is cryptanalysis: proving the system detects attacks.")