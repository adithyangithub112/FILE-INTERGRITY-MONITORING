# What is Hash Value?

A hash value, also known simply as a hash, is a fixed-size numerical or alphanumeric value generated from input data using a hash function. Hash functions take an input (or "message") and produce a unique output that represents the data. Here’s a detailed look at hash values:

A cryptographic hash is a fixed-size work string (or text) that is used as an identifier/fingerprint of some data. These are particularly useful in determining the integrity of files after they are transferred over a communication channel. Hashes are even utilized by certain OS-level processes for their work. The command processor of Windows OS (cmd.exe) provides the user with the ability to compute hashes on files/Directories via a utility command named ***Certutil.*** In this article, we will learn about computing hashes on a command prompt (cmd).

### **Description of Command**

The command *Certutil* is primarily used for working with digital certificates and not hashes. The ability to hash files is due to the presence of a *-hashfile* switch in it.

```bash
> Certutil -hashfile
-hashfile  -- Generate and display cryptographic hash over a file
```

Where *certutil* is the command, and *-hashfile* is a switch provided to it.

### **Syntax**

The -hashfile switch takes in two arguments. Firstly, the path to the file in which we are interested in getting the hash. And then the hash algorithm that we are interested in.

### **Creating a Syntax**

```bash
Certutil -hashfile (Path_to_file) [HashAlgo]
```

Where *Path_to_file* is *mandatory* (should be provided) argument and *HashAlgo* is optional argument (If not provided, defaults to SHA1). If *HashAlgo* is provided it should either be from [**SHA (Secure Hash Algorithms)**](https://www.geeksforgeeks.org/java/sha-1-hash-in-java/) or from [**MD (Message Digest)**](https://www.geeksforgeeks.org/computer-networks/what-is-the-md5-algorithm/) Cryptographic Hash families. Some of the hash algorithms allowed in the command are MD4, MD5, SHA1, SHA256, SHA512.



<img width="1467" height="353" alt="image" src="https://github.com/user-attachments/assets/e54afdc9-6fef-4a85-bda4-4e9961b6f0bb" />




---

## Key Points About Hashing

- **Fixed-Length Output**  
  Any input size produces a hash of the same length.

- **One-Way Function**  
  Hashing cannot be reversed to retrieve the original data.

- **Deterministic**  
  The same input will always generate the same hash.

- **Fast Computation**  
  Hash functions are designed to work quickly.

- **Collision Resistant**  
  Different inputs should produce different hashes (though rare collisions can occur).

- **Sensitive to Input Changes**  
  A small change in input results in a completely different hash.

---

## Common Uses of Hashing

- **Password Storage**  
  Websites store hashed passwords instead of plain text passwords.

- **Data Integrity Verification**  
  Hashes are used to confirm that files or data have not been altered.

- **Digital Signatures**  
  Hashing ensures message authenticity and integrity.

- **Blockchain Technology**  
  Hashes link blocks together securely.

- **Hash Tables and Indexing**  
  Enables fast data retrieval in databases and programming.

---

## Difference Between Hashing and Encryption

| Feature | Hashing | Encryption |
|-------|--------|-----------|
| Direction | One-way | Two-way |
| Reversible | No | Yes (with key) |
| Purpose | Data integrity & verification | Data confidentiality |
| Key Required | No | Yes |
| Example Use | Password storage | Secure communication |

---

## Summary

- Hashing is mainly used for **verification and integrity**.
- Encryption is used for **protecting data confidentiality**.
- Hashing cannot be undone, while encryption can be decrypted using a key.

---
