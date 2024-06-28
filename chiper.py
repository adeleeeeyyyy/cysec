from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(f"{file_path}.enc", 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, output_file_path):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

# Example usage
file_path = 'example.txt'
encrypt_file(file_path)
decrypt_file(f"{file_path}.enc", 'decrypted_example.txt')
