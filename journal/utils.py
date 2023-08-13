from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64
import hashlib

import environ
env = environ.Env()

def generate_random_password():
    return base64.urlsafe_b64encode(get_random_bytes(16)).decode()

def generate_hash(salt=None):
    if not salt:
        salt = get_random_bytes(16)
    return hashlib.sha256(salt).hexdigest()

def encrypt_with_aes(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.encodebytes(nonce + ciphertext).decode()

def encrypt(request, data):
    hash_salt = request.user.hash_salt
    key = PBKDF2(hash_salt, env('SECRET_KEY'), dkLen=32)
    encrypted_text = encrypt_with_aes(data, key)
    return encrypted_text

def decrypt_with_aes(encrypted_data, key):
    encoded_data = base64.decodebytes(encrypted_data.encode())
    nonce, ciphertext = encoded_data[:16], encoded_data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data.decode()

def decrypt(request, encrypted_text):
    hash_salt = request.user.hash_salt
    key = PBKDF2(hash_salt, env('SECRET_KEY'), dkLen=32)
    decrypted_text = decrypt_with_aes(encrypted_text, key)
    return decrypted_text
