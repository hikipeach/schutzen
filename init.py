import json
from pathlib import Path
import bcrypt
import os

def init():
  """
  Sets up the master password for the user and stores the hash in the vault.
  """
  overwrite()
  master_password = 'a'
  confirmed_master_password = 'b'
  while master_password != confirmed_master_password:
    master_password = input("enter the master password: ")
    confirmed_master_password = input("confirm your master password: ")
    if master_password != confirmed_master_password:
      print("error: passwords do not match")
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
  Creates a vault using an encrypted JSON value with the 
  """
  credentials = []
  data = f'{{"salt": {salt}, "hashed_password": {hashed_password}, "credentials": {credentials}}}'
  f = open('vault.json', 'w')
  json.dump(data, f, indent=4)

def does_vault_exist():
  """
  Checks if the user has a stored vault
  """
  a = Path('vault.json')
  return a.exists()

def overwrite():
  """
  Overwrites the vault if it exists
  """
  if does_vault_exist():
    print("a vault currently exists on this PC.")
    print("would you like to set up a new vault?")
    new_vault_response = input("press 'y' for yes, or any other key for no: ").lower()
    if new_vault_response == 'y':
      os.remove('vault.json')
      print('vault removed.')
    else:
      print('No changes to vault made.')
  else:
    print("a vault can not be found on your pc")
    print("setting up new vault")

init()