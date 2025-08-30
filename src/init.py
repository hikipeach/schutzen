import json
import logging
import bcrypt
import os

from utility import vault_exists
from key import create_encryption_key, encrypt_vault

logger = logging.getLogger(__name__)

def init():
  """
  Sets up the master password for the user and stores the hash in the vault.
  """
  if vault_exists():
    logger.debug("Did you want to make a new vault? Use the delete command and then init command to create a vault.")
    raise Exception("vault already initialized.")
  else:
    master_password = 'a'
    confirmed_master_password = 'b'
    logger.info("User has started initialization.")
    print("initialization starting...")

    while master_password != confirmed_master_password:
      master_password = input("Enter the master password: ")
      confirmed_master_password = input("confirm your master password: ")

      if master_password != confirmed_master_password:
        logger.info("Passwords do not match for initializing a new vault.")
        print("error: passwords do not match.")
      else:
        print("successfully confirmed master password.")

    # to hash a password it needs the password as a byte array and a salt
    byte = master_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte, salt)

    create_vault(salt, hashed_password)
    print(f"vault created. stored at {os.getcwd()}\'vault.json")
    logger.info("User created a vault.")
    print("initialization successful!")
    logger.info("Initialization complete.")

def create_vault(salt, hashed_password):
  """
  Creates a vault to store the salt and hashed password
  """
  # decode the salt and hashed password to a string so JSON can serialize it
  salt_str = salt.decode('utf-8')
  hashed_password_str = hashed_password.decode('utf-8')
  logger.info("Decoded salt and hashed password.")
  data = {"salt": salt_str, "hashed_password": hashed_password_str, "credentials": []}
  # create json file
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, 'vault.json')
  f = open(filename, 'w')
  json.dump(data, f, indent=4)
  f.close()
  # encrypt json file
  create_encryption_key()
  logger.info("Encryption key for vault created")
  encrypt_vault()
  logger.info("Vault encrypted.")


