import json
import bcrypt
import os
from key import create_encryption_key, encrypt_vault

def init():
  """
  Sets up the master password for the user and stores the hash in the vault.
  """
  if need_new_vault():
    master_password = 'a'
    confirmed_master_password = 'b'
    while master_password != confirmed_master_password:
      master_password = input("enter the master password: ")
      confirmed_master_password = input("confirm your master password: ")
      if master_password != confirmed_master_password:
        print("error: passwords do not match.")
      else:
        print("successfully confirmed master password.")
    byte = master_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte, salt)
    create_vault(salt, hashed_password)
    print(f"vault created. stored at {os.getcwd()}\'vault.json")
    print("initialization successful")

def create_vault(salt, hashed_password):
  """
  Creates a vault to store the salt and hashed password
  """
  # decode the salt and hashed password to a string so JSON can serialize it
  salt_str = salt.decode('utf-8')
  hashed_password_str = hashed_password.decode('utf-8')
  data = {"salt": salt_str, "hashed_password": hashed_password_str, "credentials": []}
  # create json file
  f = open('vault.json', 'w')
  json.dump(data, f, indent=4)
  f.close()
  # encrypt json file
  create_encryption_key()
  encrypt_vault()

def does_vault_exist():
  """
  Checks if the user has a stored vault
  """
  a = os.path.exists('vault.json')
  return a

def need_new_vault():
  """
  Overwrites the vault if it exists
  """
  if not does_vault_exist():
    print("a vault can not be found on your pc.")
    print("setting up new vault...")
    return True
  else:
    print("a vault currently exists on this PC.")
    print("would you like to set up a new vault?")
    new_vault_response = input("press 'y' for yes, or any other key for no: ").lower()
    if new_vault_response == 'y':
      os.remove('vault.json')
      print('vault removed.')
      return True
    else:
      print('no changes to vault made.')
      return False
