Building a secure password manager is a complex task that involves various security considerations. It's important to note that security is a critical aspect, and any flaws in the implementation could lead to compromised credentials. In this context, I can provide you with a simplified example using Python and its built-in libraries. However, please keep in mind that a real-world application should have a thorough security review and might require the use of external libraries and best practices.

In this example, we'll create a basic password manager that stores credentials in an encrypted file. We'll use the `cryptography` library to handle encryption and decryption. Please note that this example is meant for educational purposes and might not cover all security aspects.

```shell
pip install cryptography
```

```python
# main.py
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
```

In this example, we've created a `PasswordManager` class that handles encryption and decryption using the `cryptography` library's `Fernet` implementation. It provides methods to save and load encrypted credentials to/from a file. The credentials are encrypted using the key provided at the start.

Remember that this is a basic example, and a real-world password manager would require additional security features, such as proper key management, secure storage, strong encryption, and protection against various types of attacks.

Additionally, handling encryption and security on your own is complex and error-prone. In a production environment, you should consider using well-established libraries and frameworks designed for secure password management.