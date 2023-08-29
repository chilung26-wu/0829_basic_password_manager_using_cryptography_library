from cryptography.fernet import Fernet
import json

class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(key)

    def encrypt(self, plaintext):
        return self.cipher_suite.encrypt(plaintext.encode())

    def decrypt(self, ciphertext):
        return self.cipher_suite.decrypt(ciphertext).decode()

    def save_credentials(self, filename, credentials):
        encrypted_credentials = {}
        for key, value in credentials.items():
            encrypted_key = self.encrypt(key)
            encrypted_value = self.encrypt(value)
            encrypted_credentials[encrypted_key] = encrypted_value

        with open(filename, 'wb') as file:
            file.write(json.dumps(encrypted_credentials).encode())

    def load_credentials(self, filename):
        with open(filename, 'rb') as file:
            encrypted_credentials = json.load(file)

        credentials = {}
        for encrypted_key, encrypted_value in encrypted_credentials.items():
            key = self.decrypt(encrypted_key)
            value = self.decrypt(encrypted_value)
            credentials[key] = value

        return credentials

if __name__ == "__main__":
    # Generate a random key for encryption (keep this key safe!)
    key = Fernet.generate_key()
    password_manager = PasswordManager(key)

    credentials = {
        "example@gmail.com": "pa$$w0rd",
        "user123": "secretp@ss"
    }

    encrypted_filename = "encrypted_credentials.json"
    password_manager.save_credentials(encrypted_filename, credentials)

    loaded_credentials = password_manager.load_credentials(encrypted_filename)
    for key, value in loaded_credentials.items():
        print(f"Username: {key}, Password: {value}")
