import hashlib
import random

# HASH 
def sha256(data):
    return hashlib.sha256(data).hexdigest()

# XOR SYMMETRIC ENCRYPTION
def xor_encrypt(data, key):
    return bytes([b ^ key for b in data])

def xor_decrypt(data, key):
    return bytes([b ^ key for b in data])

# SUBSTITUTION CIPHER (CAESAR)
def caesar_encrypt(text, shift=3):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# DIGITAL SIGNATURE ILLUSTRATION
def fake_generate_keys():
    private_key = "my_private_key_123"
    public_key = "my_public_key_123"
    return private_key, public_key

def fake_sign(private_key, data):
    # A simple “signature” = hash(private_key + data)
    return sha256((private_key + data).encode())

def fake_verify(public_key, data, signature):
    # Match with the same pattern (this is only for illustration)
    expected = sha256(("my_private_key_123" + data).encode())
    return expected == signature

# MAIN PROGRAM
def main():
    print("Simple Secure Data Transmission Demo\n")

    msg = input("Enter a message: ")
    msg_bytes = msg.encode()

    # Original hash
    h1 = sha256(msg_bytes)
    print("Original SHA-256 hash:", h1)

    # Symmetric encryption using XOR
    key = random.randint(1, 255)
    encrypted = xor_encrypt(msg_bytes, key)
    print("\nEncrypted (XOR):", encrypted)

    decrypted = xor_decrypt(encrypted, key)
    print("Decrypted:", decrypted.decode())

    # Integrity check
    h2 = sha256(decrypted)
    print("Integrity OK?", h1 == h2)

    # Caesar substitution cipher
    c = caesar_encrypt(msg)
    print("\nCaesar Encrypted:", c)
    print("Caesar Decrypted:", caesar_decrypt(c))

    # Digital signature illustration
    priv, pub = fake_generate_keys()
    signature = fake_sign(priv, msg)
    print("\nDigital Signature:", signature)
    print("Signature Valid?", fake_verify(pub, msg, signature))

if __name__ == "__main__":
    main()
