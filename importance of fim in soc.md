### What is File Integrity Monitoring (FIM)?

**File Integrity Monitoring (FIM)** is a security process that:

- Establishes a **baseline state** of critical files
- Continuously monitors files for **unauthorized changes**
- Alerts security teams when file integrity is compromised

It typically uses **cryptographic hashing** (MD5, SHA-256, etc.) to detect even the smallest modification.

---

### Why FIM Is Critical in a SOC

In a **Security Operations Center (SOC)**, FIM plays a vital role in **threat detection, incident response, and compliance**.

### 1. **Early Attack Detection**

- Attackers often modify:
    - System binaries
    - Configuration files
    - Log files
- FIM helps detect:
    - Malware persistence
    - Rootkits
    - Web shell injections

### 2. **Insider Threat Monitoring**

- Detects unauthorized changes by:
    - Privileged users
    - Compromised admin accounts

### 3. **Incident Response Support**

- SOC analysts can:
    - Identify **what changed**
    - Determine **when it changed**
    - Investigate **who or what caused the change**

### 4. **Regulatory Compliance**

FIM is often **mandatory** for:

- PCI-DSS
- HIPAA
- SOX
- ISO 27001

### 5. **Maintaining System Trust**

- Ensures critical systems remain in a **known-good state**
- Prevents silent tampering that could go unnoticed for long periods
