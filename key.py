# Module for key functions to read/write, encrypting and decrypting vault
import os
from cryptography.fernet import Fernet

def create_encryption_key():
  key = Fernet.generate_key()
  with open('key.env', 'wb') as vault_key:
    vault_key.write(key)

def get_encryption_key():
  with open('key.env', 'rb') as vault_key:
    key = vault_key.read()
  vault_key.close()
  return key

def encrypt_vault():
    key = get_encryption_key()
    f = Fernet(key)
    with open('vault.json', 'rb') as vault_json:
        vault = vault_json.read()
    encrypted_vault = f.encrypt(vault)
    vault_json.close()
    with open('vault.json', 'wb') as enc_vault_json:
        enc_vault_json.write(encrypted_vault)
    enc_vault_json.close()