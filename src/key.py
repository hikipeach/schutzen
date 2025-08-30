# Module for key functions to read/write, encrypting and decrypting vault
import logging
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)
logging.basicConfig(filename='schutzen.log', encoding='utf-8', level=logging.INFO)
def create_encryption_key():
  key = Fernet.generate_key()
  logger.info("Key generation complete.")

  with open('../config/key.env', 'wb') as vault_key:
    vault_key.write(key)

  logger.info("Writing complete. Closing file.")
  vault_key.close()

def get_encryption_key():
  logger.info("Opening file for reading encrypted key")
  with open('../config/key.env', 'rb') as vault_key:
    logger.info("Reading key...")
    key = vault_key.read()

  logger.info("Reading key completed. Closing file.")
  vault_key.close()
  return key

def encrypt_vault():
    key = get_encryption_key()
    f = Fernet(key)

    logger.info("Opening file for reading from the vault.")
    with open('vault.json', 'rb') as vault_json:
        vault = vault_json.read()

    logger.info("Encrypted vault.")
    encrypted_vault = f.encrypt(vault)

    logger.info("Closing file for reading from the vault.")
    vault_json.close()

    logger.info("Opening file for writing to the encrypted vault.")
    with open('vault.json', 'wb') as enc_vault_json:
        enc_vault_json.write(encrypted_vault)

    logger.info("Closing file for encrypting vault.")
    enc_vault_json.close()

def decrypt_vault():
    key = get_encryption_key()
    f = Fernet(key)


    logger.info("Opening file for reading encrypted vault")
    with open('vault.json', 'rb') as enc_vault_json:
        encrypted_vault = enc_vault_json.read()

    logger.info("Decrypted vault.")
    vault = f.decrypt(encrypted_vault)

    logger.info("Reading complete. Closing file.")
    enc_vault_json.close()
    return vault