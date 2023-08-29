Building a secure password manager is a complex task that involves various security considerations. It's important to note that security is a critical aspect, and any flaws in the implementation could lead to compromised credentials. In this context, I can provide you with a simplified example using Python and its built-in libraries. However, please keep in mind that a real-world application should have a thorough security review and might require the use of external libraries and best practices.

In this example, we'll create a basic password manager that stores credentials in an encrypted file. We'll use the `cryptography` library to handle encryption and decryption. Please note that this example is meant for educational purposes and might not cover all security aspects.

```shell
pip install cryptography
```

```python
# main.py
# 導入必要的模組
from cryptography.fernet import Fernet  # 導入 Fernet 模組，用於加密解密
import json  # 導入 json 模組，用於處理 JSON 格式的資料

# 建立一個名為 PasswordManager 的類別
class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(key)

    # 加密方法：使用 cipher_suite 對輸入的文字進行加密
    def encrypt(self, plaintext):
        return self.cipher_suite.encrypt(plaintext.encode())

    # 解密方法：使用 cipher_suite 對輸入的密文進行解密，並轉換為原始文字
    def decrypt(self, ciphertext):
        return self.cipher_suite.decrypt(ciphertext).decode()

    # 儲存帳號密碼資訊
    def save_credentials(self, filename, credentials):
        encrypted_credentials = {}
        for key, value in credentials.items():
            encrypted_key = self.encrypt(key)  # 對帳號進行加密
            encrypted_value = self.encrypt(value)  # 對密碼進行加密
            encrypted_credentials[encrypted_key] = encrypted_value

        # 將加密後的資料儲存到檔案中
        with open(filename, 'wb') as file:
            file.write(json.dumps(encrypted_credentials).encode())

    # 讀取並解密帳號密碼資訊
    def load_credentials(self, filename):
        with open(filename, 'rb') as file:
            encrypted_credentials = json.load(file)  # 從檔案中載入加密後的資料

        credentials = {}
        for encrypted_key, encrypted_value in encrypted_credentials.items():
            key = self.decrypt(encrypted_key)  # 解密帳號
            value = self.decrypt(encrypted_value)  # 解密密碼
            credentials[key] = value

        return credentials

# 主程式開始
if __name__ == "__main__":
    # 產生一個隨機金鑰，用於加密解密（請保管好這個金鑰！）
    key = Fernet.generate_key()

    # 建立 PasswordManager 的實例，並傳入金鑰
    password_manager = PasswordManager(key)

    # 要儲存的帳號密碼資訊
    credentials = {
        "example@gmail.com": "pa$$w0rd",
        "user123": "secretp@ss",
        "aaa": "bbb",
        "asdf": "zxcv"
    }

    # 指定儲存加密後資料的檔案名稱
    encrypted_filename = "encrypted_credentials.json"

    # 呼叫 PasswordManager 的儲存方法，將加密後的資料儲存到檔案中
    password_manager.save_credentials(encrypted_filename, credentials)

    # 呼叫 PasswordManager 的讀取方法，讀取並解密儲存的帳號密碼資訊
    loaded_credentials = password_manager.load_credentials(encrypted_filename)

    # 顯示解密後的帳號密碼資訊
    for key, value in loaded_credentials.items():
        print(f"Username: {key}, Password: {value}")
```

In this example, we've created a `PasswordManager` class that handles encryption and decryption using the `cryptography` library's `Fernet` implementation. It provides methods to save and load encrypted credentials to/from a file. The credentials are encrypted using the key provided at the start.

Remember that this is a basic example, and a real-world password manager would require additional security features, such as proper key management, secure storage, strong encryption, and protection against various types of attacks.

Additionally, handling encryption and security on your own is complex and error-prone. In a production environment, you should consider using well-established libraries and frameworks designed for secure password management.