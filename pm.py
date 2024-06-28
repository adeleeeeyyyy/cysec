from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt password
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())

# Function to decrypt password
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()

# Example usage
password = "my_secure_password"
encrypted_password = encrypt_password(password)
print(f"Encrypted: {encrypted_password}")
print(f"Decrypted: {decrypt_password(encrypted_password)}")
