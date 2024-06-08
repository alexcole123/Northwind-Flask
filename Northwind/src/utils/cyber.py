from hashlib import sha512 # SHA = Secure Hashing Algorithm - sha512 is a powerful hashing algorithm.
from .app_config import AppConfig

class Cyber:

    @staticmethod
    def hash(plain_text):
        encoded_text = plain_text.encode("UTF-8") + AppConfig.passwords_salt.encode("UTF-8")
        hashed_text = sha512(encoded_text).hexdigest()
        return hashed_text
