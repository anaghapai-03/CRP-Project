# CRP-Project
# SecureSign — Digital Signature System
## Pure cryptography. No APIs. No server. No libraries.

---

## What this project is

A complete browser-based digital signature system using:
- **RSA-2048** key generation (real 2048-bit primes)
- **SHA-256** document hashing
- **RSA-PSS** signing and verification
- All via the browser's built-in **Web Crypto API** (zero dependencies)

---

## How to run (3 options — pick one)

---

### OPTION 1 — VS Code Live Server (recommended, 1 click)

1. Open VS Code
2. Install the **Live Server** extension:
   - Click Extensions icon (left sidebar) or press `Ctrl+Shift+X`
   - Search: `Live Server`
   - Install by Ritwick Dey
3. Open the `securesign/` folder in VS Code:
   `File → Open Folder → select securesign folder`
4. Right-click `index.html` in Explorer panel
5. Click **"Open with Live Server"**
6. Browser opens automatically at `http://127.0.0.1:5500`
7. Done ✓

---

### OPTION 2 — Python HTTP Server (no extensions needed)

Open terminal in the `securesign/` folder, then run:

```bash
# Python 3 (most systems)
python -m http.server 8080

# Python 2 (older systems)
python -m SimpleHTTPServer 8080
```

Then open browser: `http://localhost:8080`

To stop the server: `Ctrl + C` in terminal.

---

### OPTION 3 — Node.js HTTP Server

```bash
# Install once globally
npm install -g http-server

# Run from securesign/ folder
http-server -p 8080

# Or with npx (no install needed)
npx http-server -p 8080
```

Open: `http://localhost:8080`

---

## Why you CANNOT just double-click index.html

Web Crypto API requires a secure context (`http://localhost` or `https://`).
Opening as `file:///...` gives a security error. You need a local server.

---

## Using the app — step by step

### Step 1: Generate Keys
1. Go to **Key Generation** tab
2. Enter a name (e.g. "Alice")
3. Click **Generate RSA-2048 Key Pair**
4. Wait 1-2 seconds — your private key and public key appear
5. Repeat with a different name (e.g. "Bob") for multi-signing

### Step 2: Sign a Document
1. Go to **Sign Document** tab
2. Type your document text
3. Select your key from the dropdown
4. Click **Sign Document**
5. See: SHA-256 hash + RSA signature + visual fingerprint
6. Click **Export .json bundle** to save the signed file

### Step 3: Verify
1. Go to **Verify Signature** tab
2. Paste the JSON bundle (or load the exported file)
3. Click **Verify Bundle**
4. See: VALID or INVALID + full report

### Step 4: Tamper Test (see the crypto in action)
1. Sign a document first
2. Scroll to **Tamper Test Lab** on the Verify page
3. Click **Load last signed** → **Tamper document** → **Verify tampered**
4. Watch it fail — changing 1 character invalidates the signature

### Step 5: Multi-Party Signing
1. Generate keys for Alice AND Bob (Key Generation)
2. Go to **Multi-Sign Contract** tab
3. Click **Add my signature** twice (Alice signs, then Bob signs)
4. Click **Verify all signatures**

---

## Crypto operations happening in your browser

| What | How | Code |
|------|-----|------|
| Key generation | RSA-PSS 2048-bit | `crypto.subtle.generateKey()` |
| Document hash | SHA-256 | `crypto.subtle.digest('SHA-256', ...)` |
| Signing | RSA-PSS with salt=32 | `crypto.subtle.sign({name:'RSA-PSS',...})` |
| Verification | RSA-PSS verify | `crypto.subtle.verify(...)` |
| Key export | PKCS#8 / SPKI PEM | `crypto.subtle.exportKey()` |

No npm. No node_modules. No external requests. Just 1 HTML file.

---

## Project structure

```
securesign/
│
└── index.html          ← entire app (HTML + CSS + JS, ~600 lines)
└── README.md           ← this file
```

---

## Troubleshooting

**"SecurityError: The operation is insecure"**
→ You opened the file directly. Use a local server (Option 1, 2, or 3 above).

**"Failed to fetch" or fonts don't load**
→ Google Fonts needs internet. App works fine without fonts, just looks different.

**Buttons not responding**
→ Try a modern browser: Chrome 90+, Firefox 90+, Edge 90+, Safari 15+.

**generateKey takes forever**
→ Normal on older hardware. RSA-2048 takes 1–3 seconds.
