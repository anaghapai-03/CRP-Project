# SecureSign
### Browser-Based Cryptographic Document Signing System

> Sign documents with RSA-2048 · Verify authenticity with SHA-256 · Encrypt with AES-256-GCM · All in your browser

---

## What It Is

SecureSign is a browser-based tool for digitally signing, verifying, and encrypting documents. It implements RSA-2048, SHA-256, and AES-256-GCM from their mathematical foundations in pure JavaScript — no libraries, no frameworks, no external dependencies.

Everything runs locally on your computer. No data is sent to any server.

---

## The Problem It Solves

When you send a digital document, there is no built-in way to prove:

- **Who sent it** — anyone can claim to be anyone
- **It wasn't changed** — data can be modified in transit
- **Only the recipient can read it** — plain files are readable by anyone who intercepts them

SecureSign solves all three using real cryptography.

---

## Algorithms Used

| Algorithm | Purpose | How It Works |
|---|---|---|
| **RSA-2048** | Digital signatures | `s = m^d mod n` — private key signs, public key verifies |
| **SHA-256** | Document fingerprinting | 64 rounds of bitwise compression → 256-bit hash |
| **AES-256-GCM** | Symmetric encryption | 14-round block cipher + GHASH authentication tag |
| **PBKDF2-SHA256** | Password to key | 100,000 HMAC-SHA256 iterations |

---

## Features

- **Key Generation** — Real RSA-2048 key pairs using Miller-Rabin prime testing
- **Sign Document** — SHA-256 hash + RSA sign → export as JSON bundle
- **Verify Signature** — RSA verify + hash comparison → VALID or INVALID
- **Tamper Test** — Change one character → watch signature break
- **AES-256-GCM Encryption** — Encrypt signed bundles with a password
- **Multi-Party Signing** — Multiple signers on the same document
- **How It Works** — Live SHA-256 demo, RSA calculator, AES visualiser

---

## File Structure

```
securesign/
│
├── index.html           ← entire application (HTML + CSS + JS)
├── wireshark_demo.py    ← Python server for Wireshark demonstration
└── README.md            ← this file
```

---

## Requirements

- Any modern browser — Chrome 90+, Firefox 90+, Edge 90+, Safari 15+
- Python 3 (for the local server)
- No npm, no pip packages, no installation needed

---

## How to Run

### Option 1 — VS Code Live Server (Easiest)

**Step 1** — Open VS Code

**Step 2** — Open the project folder
```
File → Open Folder → select the securesign folder
```

**Step 3** — Install Live Server extension
```
Ctrl+Shift+X → search "Live Server" → Install (by Ritwick Dey)
```

**Step 4** — Launch the app
```
Right-click index.html in the file explorer
→ Click "Open with Live Server"
→ Browser opens at http://127.0.0.1:5500
```

---

### Option 2 — Python HTTP Server

Open terminal in the securesign folder and run:

```bash
python -m http.server 8080
```

Then open your browser and go to:
```
http://localhost:8080
```

To stop the server press `Ctrl+C`.

---

### Option 3 — Node.js

```bash
npx http-server -p 8080
```

Then open:
```
http://localhost:8080
```

---

### Why You Cannot Double-Click index.html

Opening the file directly gives a `file://` URL. The browser blocks the cryptographic random number generator (`crypto.getRandomValues`) on `file://` for security reasons. A local HTTP server provides the `http://localhost` context that allows it to work.

---

## How to Use

### Step 1 — Generate a Key Pair

1. Go to the **Key Generation** tab
2. Enter your name (e.g. `Alice`)
3. Click **Generate RSA-2048 Key Pair**
4. Wait 20–60 seconds (finding real 1024-bit primes takes time)
5. Your private key and public key appear in PEM format

> Keep your private key secret. Share your public key freely.

---

### Step 2 — Sign a Document

1. Go to **Sign Document** tab
2. Type your document (e.g. `Pay Bob Rs 50,000 by June 30 2026`)
3. Select your key from the dropdown
4. Click **Sign Document**
5. You see:
   - SHA-256 fingerprint (64 hex characters)
   - RSA signature (first 80 characters shown)
   - Visual fingerprint (32 coloured squares = 32 bytes of hash)
6. Click **Download .json** to export the signed bundle

---

### Step 3 — Verify a Signature

1. Go to **Verify Signature** tab
2. Paste the JSON bundle into the text area
3. Click **Verify**
4. Result shows **VALID ✓** or **INVALID ✗** with full report

---

### Step 4 — Tamper Test (Cryptanalysis Demo)

1. Sign a document first
2. Go to Verify tab → scroll to **Tamper Test Lab**
3. Click **Load last signed**
4. Click **Tamper document** (changes a number in the document)
5. Click **Verify tampered**
6. Result: **INVALID ✗** — proves any change breaks the signature

---

### Step 5 — AES-256-GCM Encryption

**Encrypt:**
1. Go to **AES-256 Encrypt** tab
2. Enter your message
3. Enter a password
4. Click **Encrypt with AES-256-GCM**
5. You see: salt, IV, ciphertext, auth tag, and full JSON bundle
6. Copy the bundle

**Decrypt:**
1. Click **→ Go to Decrypt** or switch to Decrypt tab
2. Paste the bundle
3. Enter the same password
4. Click **Decrypt**
5. Original message recovered

---

### Step 6 — Multi-Party Signing

1. Generate keys for **Alice** and **Bob** (Key Generation, do it twice)
2. Go to **Multi-Sign** tab
3. Type a contract document
4. Click **+ Add my signature** (Alice signs)
5. Click **+ Add my signature** again (Bob signs)
6. Click **Verify all signatures**
7. Both signatures verified independently

---

### Step 7 — Sign then Encrypt (Combined)

1. Sign a document (Step 2)
2. On the Sign page scroll down to **"Optional — Encrypt this signature"**
3. Enter a password
4. Click **Encrypt Signed Bundle**
5. Go to Verify tab → **Encrypted Bundle** tab
6. Paste the encrypted bundle + enter password
7. Click **Decrypt + Verify**
8. App decrypts then verifies RSA signature in one step

---

## Wireshark Demo

This demonstrates cryptanalysis — showing what an attacker sees on the network with and without encryption.

**Step 1** — Run the demo server

```bash
python wireshark_demo.py
```

Output:
```
SecureSign — Wireshark Demo Server
Running at: http://localhost:9090

Endpoints:
  http://localhost:9090/          → home page
  http://localhost:9090/plain     → plain signed bundle
  http://localhost:9090/encrypted → AES encrypted bundle
  http://localhost:9090/tampered  → tampered bundle
  http://localhost:9090/hashes    → SHA-256 hash comparison
```

**Step 2** — Set up Wireshark

```
Open Wireshark
→ Select Loopback interface
→ Filter: tcp.port == 9090
→ Click blue shark fin to start capture
```

**Step 3** — Run the three demos

| Endpoint | What Wireshark Shows | What It Proves |
|---|---|---|
| `/plain` | Full document text visible | Plain HTTP has no confidentiality |
| `/encrypted` | Only random hex ciphertext | AES-256-GCM hides all content |
| `/tampered` | Changed amount, same signature | Attacker cannot forge RSA signature |
| `/hashes` | Two completely different hashes | SHA-256 avalanche effect |

**Step 4** — Follow TCP Stream

```
Right-click any HTTP packet
→ Follow → TCP Stream
→ Screenshot what you see
```

---

## What the JSON Bundle Looks Like

A signed document exported from SecureSign:

```json
{
  "document": "Pay Bob Rs 50,000 by June 30 2026",
  "signature": "3a4f9c2b1d...(512 hex characters)...",
  "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjAN...\n-----END PUBLIC KEY-----",
  "signer": "Alice",
  "timestamp": "2026-06-10T10:00:00.000Z",
  "algorithm": "RSA-PKCS1v15-SHA256",
  "keySize": 2048
}
```

An AES-encrypted signed bundle:

```json
{
  "encrypted": {
    "salt": "a3f9b2c1d4e56789...",
    "iv": "1a2b3c4d5e6f...",
    "ciphertext": "8f3a9b2c...(random hex)...",
    "tag": "abcdef0123456789..."
  },
  "algorithm": "RSA-PKCS1v15-SHA256 + AES-256-GCM",
  "kdf": "PBKDF2-SHA256-100000"
}
```

---

## Security Properties

| Property | Guarantee | Algorithm |
|---|---|---|
| Authenticity | Only private key holder could sign | RSA-2048 |
| Integrity | Any change breaks signature | SHA-256 |
| Confidentiality | Only password holder can decrypt | AES-256-GCM |
| Non-repudiation | Signer cannot deny signing | RSA-2048 |
| Tamper evidence | Auth tag detects ciphertext changes | GCM |
| Brute-force resistance | Each password guess costs 100k operations | PBKDF2 |

---

## Real World Applications

- **Legal contracts** — sign, timestamp, verify
- **Medical prescriptions** — tamper-evident, multi-sign
- **Certificate verification** — college degrees, government documents
- **Secure file transfer** — sign + encrypt before sending
- **Multi-party agreements** — each party signs independently
- **Audit trails** — signed records with timestamps

---

## Tools Used for Demonstration

| Tool | How It Is Used |
|---|---|
| **Wireshark** | Capture HTTP packets to show plain vs encrypted traffic |
| **GnuPG** | Command-line RSA signing to cross-verify our implementation |
| **Hashcat** | Show PBKDF2 makes brute-force 100,000x slower |
| **CrypTool Online** | Visual AES round demonstration and hash analysis |
| **CyberChef** | Cross-verify SHA-256 output matches our implementation |

---

## Limitations

- Key generation takes 20–60 seconds (pure JavaScript prime finding is slow)
- Keys are lost when the browser tab is closed (no persistent storage)
- No Certificate Authority — cannot verify real-world identity of key holders
- PKCS#1 v1.5 padding used instead of RSA-PSS (simpler but not latest standard)
- AES encryption takes 15–40 seconds (PBKDF2 at 100k iterations in JavaScript)

---

## Privacy

- Private keys never leave your device
- No data sent to any server
- Closing the tab clears all keys (by design)
- All cryptographic operations happen in your browser

---

*SecureSign — Built with pure cryptographic mathematics.*
*RSA-2048 · SHA-256 · AES-256-GCM · PBKDF2*