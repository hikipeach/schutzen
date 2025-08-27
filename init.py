import doctest
import json
from pathlib import Path
from cryptography.fernet import Fernet
import bcrypt

def init():
  """
  Sets up the master password for the user and stores the hash in the vault.
  """
  overwrite()
  while master_password != confirmed_master_password:
    master_password = input("Please enter the master password:")
    confirmed_master_password = input("Please confirm your master password:")
    if master_password != confirmed_master_password:
      print("Confirmed master password does not match original master password.")
    else:
      print("Successfuly confirmed master password.")
  bytes = master_password.encode('utf-8')
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(bytes, salt)
  create_vault(salt, hashed_password)

def create_vault(salt, hashed_password):
  """
  Creates a vault using an encrypted JSON value with the 
  """
  f = open('vault.json.enc', 'x')
  encrypted_vault = encrypt_vault(salt, hashed_password)
  f.write(encrypted_vault)
  f.close()

def encrypt_vault(salt, hashed_password):
  """
  Encrypts the vault with a key so that it can not be decrypted without it
  """
  data = {"salt": salt, "hashed_password": hashed_password, "credentials": []}
  key = Fernet.generate_key()
  f = Fernet(key)
  encrypted_data = f.encrypt(json.dumps(data))
  return encrypted_data

def does_vault_exist():
  """
  Checks if the user has a stored vault
  """
  a = Path('vault.json.enc')
  return a.exists()

def overwrite():
  """
  Overwrites the vault if it exists
  """
  if does_vault_exist():
    print("A vault currently exists on this PC.")
    print("Would you like to set up a new vault?")
    new_vault_response = input("[y]es or enter any key for no.").lower()
    return new_vault_response == 'y'
  else:
    print("Vault not found. Setting up new vault for the first time.")

