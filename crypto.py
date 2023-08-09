from cryptography.fernet import Fernet

class SymmetricEncryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data):
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
