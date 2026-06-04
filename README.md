# SecureSign — Digital Signature System

**Pure cryptography. No APIs. No dependencies. Just cryptography.**

Sign documents with RSA-2048, prove they haven't been tampered with using SHA-256 hashing and digital signatures.

## Quick Start

```bash
# Run a local server
python -m http.server 8080
```

Then open: `http://localhost:8080`

## What It Does

1. **Generate Keys** — Create RSA-2048 key pairs (private + public)
2. **Sign Documents** — Hash with SHA-256, sign with private key
3. **Verify Signatures** — Check authenticity with public key
4. **Detect Tampering** — Change 1 character = signature breaks ✗
5. **Multi-Sign** — Multiple people sign the same document

## How to Use

| Task | Steps |
|------|-------|
| **Sign a document** | Generate key → Go to Sign → Paste document → Sign → Export JSON |
| **Verify signature** | Go to Verify → Load JSON → Click Verify |
| **Prove tampering breaks signatures** | Sign → Change 1 char → Verify → See ❌ INVALID |

## Tech Inside

- **RSA-2048** — Key generation (real 2048-bit primes)
- **SHA-256** — Document fingerprinting  
- **RSA-PSS** — Signing and verification
- **Web Crypto API** — All in browser, zero dependencies

## File Structure

```
.
├── index.html       ← entire app (HTML + CSS + JS)
├── README.md        ← this file
```

## Requirements

- Modern browser (Chrome 90+, Firefox 90+, Safari 15+, Edge 90+)
- Local HTTP server (can't run as `file://`)
- That's it!

## Why This Works

Your **private key never leaves your device**. Only you can create valid signatures. When you sign, the signature is mathematically locked to that exact document. Change anything → signature breaks. No forgery possible. 🔒

# SecureSign — Digital Signature System

## What Is This?

SecureSign is a **browser-based tool** for digitally signing documents and encrypting them. Everything happens **locally on your computer** — no servers, no internet needed, no accounts.

---

## The Problem It Solves

Imagine you send a document to Bob. How does Bob know:
1. **It came from you?** (Not someone pretending to be you)
2. **It wasn't changed?** (Nobody modified it along the way)
3. **Only Bob can read it?** (It's secret, not visible to everyone)

SecureSign solves all three problems using **real cryptography**.

---

## How It Works (Plain English)

### **Part 1: Digital Signatures (RSA)**

Think of a digital signature like a tamper-proof seal on an envelope:

1. **Generate Keys**
   - You create two special numbers: a **private key** (secret, like your password) and a **public key** (you can share it with anyone)
   - These use 2048-bit numbers (huge numbers, impossible to guess)

2. **Sign a Document**
   - You write a message
   - Your private key "signs" it (creates a unique mark only you can make)
   - The signature proves: "I wrote this, and I own the private key"

3. **Verify the Signature**
   - Anyone with your public key can verify the signature
   - If someone changes even 1 letter → the signature breaks
   - If someone forges your name → the signature fails

**Real-world example:** Banks use this to sign financial documents. If a hacker tries to change "$1000" to "$10,000", the signature fails.

---

### **Part 2: Encryption (AES-256-GCM)**

Now you want to make the document **secret** — only Bob should be able to read it.

1. **Choose a Password**
   - You and Bob agree on a secret password
   - The app turns this password into a cryptographic key

2. **Encrypt the Signature**
   - The app locks the signed document using AES-256-GCM (a super-strong cipher)
   - Encrypted = scrambled into meaningless data
   - Only someone with the password can unlock it

3. **Send It**
   - Send the encrypted bundle to Bob (safe to send via email, internet, etc.)
   - Even if hackers intercept it, they see only garbage
   - Bob uses the password to decrypt it

**Real-world example:** WhatsApp, Signal, and Gmail all use similar encryption.

---

## Complete Workflow

```
You                                    Bob
|                                      |
1. Write a message                     
2. Sign it with your private key       
3. Encrypt with AES (password)         
4. Send encrypted bundle ─────────────>
                                       5. Decrypt with password
                                       6. Verify your signature
                                       7. Read the message
```

---

## Key Features

✅ **RSA-2048 Signing** — Industry-standard digital signatures  
✅ **AES-256-GCM Encryption** — Military-grade encryption  
✅ **PBKDF2 Key Derivation** — Password hashing (100,000 iterations = slow for hackers)  
✅ **Zero Dependencies** — No libraries, no APIs, pure browser crypto  
✅ **No Server** — Everything runs locally on your device  
✅ **Light Theme UI** — Clean, simple, modern design  
✅ **Multi-Sig Support** — Multiple people can sign the same contract  

---

## How to Use

### Step 1: Generate a Key Pair
- Go to **Key Generation**
- Enter your name (e.g., "Alice")
- Click **Generate RSA-2048 Key Pair**
- Wait 1-2 seconds
- You get a private key (keep secret) and public key (share freely)

### Step 2: Sign a Document
- Go to **Sign Document**
- Type your message
- Select your key
- Click **Sign Document**
- You get:
  - SHA-256 hash (fingerprint of the message)
  - RSA signature (proof only you can make)
  - Visual fingerprint (32 colored squares)

### Step 3: Encrypt the Signed Document
- Set a password (e.g., "SuperSecret123")
- Click **Encrypt with AES-256-GCM**
- You get an encrypted bundle (looks like random data)
- Download or copy it

### Step 4: Send It
- Email it to Bob, upload it, send via any channel
- Only someone with the password can decrypt it
- Only someone with your public key can verify the signature

### Step 5: Recipient Decrypts & Verifies
- Bob pastes the encrypted bundle
- Enter the password
- Click **Decrypt**
- Bob sees your message
- The signature verifies: "This came from Alice, unchanged"

---

## Why Is This Secure?

| Algorithm | Strength | Why |
|-----------|----------|-----|
| **RSA-2048** | 2048-bit | Takes 1000+ years to crack with today's computers |
| **AES-256-GCM** | 256-bit | Takes trillions of years to crack by brute force |
| **SHA-256** | 256-bit | Impossible to forge the same hash (1 in 2^256 chance) |
| **PBKDF2** | 100k iterations | Makes guessing your password 100,000x slower |

---

## Technical Details

- **Language:** Pure JavaScript (no frameworks, no npm packages)
- **Crypto:** Browser's built-in Web Crypto API
- **Key Size:** 2048-bit RSA, 256-bit AES
- **Signature Scheme:** RSA-PSS (Probabilistic Signature Scheme)
- **Hash:** SHA-256
- **Encryption Mode:** AES-256-GCM (includes authentication)
- **Key Derivation:** PBKDF2-SHA256 (100,000 iterations)

---

## Real-World Use Cases

### 1. **Legal Contracts**
- Alice signs a contract
- Encrypts it with a password shared with Bob
- Bob decrypts and verifies Alice signed it
- Both have proof of agreement

### 2. **Confidential Messages**
- Send encrypted, signed emails
- Recipient knows it came from you (signature)
- No one else can read it (encryption)

### 3. **Multi-Party Agreements**
- Multiple people sign the same document
- Each signature is independent and verifiable
- Example: Alice, Bob, and Charlie all sign a contract

### 4. **Tamper Detection**
- Load a signed document
- Change 1 character
- Try to verify
- Signature fails — proof of tampering

---

## What You CAN'T Do

❌ Recover a lost private key (it's gone forever)  
❌ Decrypt without the password (no backdoor)  
❌ Forge someone else's signature (mathematically impossible)  
❌ Crack a 2048-bit RSA key (not with today's tech)  

---

## Privacy Note

✅ **Your keys never leave your device**  
✅ **No data is sent to any server**  
✅ **Refresh the page = lose session keys** (intentional, for security)  
✅ **All crypto happens in your browser**  
✅ **Open source — you can audit the code**  

---

## How to Run

**Option 1: VS Code Live Server (Easiest)**
```bash
1. Install "Live Server" extension
2. Right-click index.html
3. Click "Open with Live Server"
4. Browser opens at http://127.0.0.1:5500
```

**Option 2: Python HTTP Server**
```bash
python -m http.server 8080
# Then open http://localhost:8080
```

**Option 3: Node.js**
```bash
npx http-server -p 8080
# Then open http://localhost:8080
```

---

## Example Workflow

```
Alice creates a contract:
  "I agree to pay Bob $1000 by June 30, 2026"

Alice signs it:
  SHA-256 hash: 7b99896e19f6d826535d9694e0b9fef95dd48bec755fc50e8401707459c62329
  RSA signature: 592cf6b1896e8dfe... (256 bytes)

Alice encrypts with password "BobbySuperSecret":
  Encrypted bundle: {"iv":"...", "ciphertext":"...", "tag":"..."}

Alice sends to Bob via email

Bob decrypts with password "BobbySuperSecret":
  Gets back the signed document

Bob verifies the signature with Alice's public key:
  ✓ Signature VALID
  ✓ Document authentic
  ✓ Unmodified
```

## Summary

**SecureSign = Digital signatures + AES encryption in your browser**

- 🔐 **Sign** documents with RSA-2048 (prove authenticity)
- 🔒 **Encrypt** signatures with AES-256 (ensure privacy)
- 📱 **No server** — everything local
- ⚡ **Instant** — runs entirely in your browser
- 🎓 **Educational** — learn real cryptography

Use it for:
- Signing legal documents
- Encrypting sensitive messages
- Multi-party contracts
- Testing cryptographic concepts
- Learning how real security works



**Made with pure cryptography. No APIs. No servers. No dependencies.**  
**Everything happens in your browser.**

