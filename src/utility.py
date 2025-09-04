import os
import pyperclip3
import asyncio
import json
import logging

from cryptography.fernet import Fernet
from src import key

logger = logging.getLogger(__name__)

def vault_exists():
  """
  Checks if the user has a stored vault
  """
  a = os.path.exists('vault.json')
  return a


#ascynchronously clears clipboard after 30 seconds
def copy_password(password):
  """
  Copies password to the clipboard
  """
  pyperclip3.copy(password)
  print("your password has been copied to your clipboard and will be cleared after 30 seconds.")

async def clear_password():
  """
  Clears clipboard after 30 seconds
  """
  # Needs to be asynchronous because this should not affect them using the program as a whole
  await asyncio.sleep(30)
  pyperclip3.clear()
  return pyperclip3.paste()


def encrypt_password(password):
  """
  Encrypts password using symmetric encryption
  """
  f = Fernet(key.get_encryption_key())
  byte = password.encode('utf-8')
  return f.encrypt(byte)

def decrypt_password(password):
  """
  Decrypts password using symmetric encryption
  """
  f = Fernet(key.get_encryption_key())
  return f.decrypt(password).decode()

async def logout():
  """
  Logs out after 2 minutes
  """
  await asyncio.sleep(120)

def store_credential(credential):
  # store obj.account to vault
  account = credential.account
  vault_dict, vault_len = get_vault_info()

  if vault_len == 0:
    vault_dict["credentials"].append(account)
    print(f"added new website: {credential.website}")
    logger.info(f"Added {credential.website} to storage")
  else:
    #update vault_dict["credentials"][current_site_idx] to account
    arr_credentials = vault_dict["credentials"]

    for i in range(0, len(arr_credentials)):
      arr_account = vault_dict["credentials"][i]
      for j in range(0, len(arr_account)):
        account = arr_account[j]
        for k, v in account.items():
          if k == credential.website:
            vault_dict["credentials"][i] = v
  logger.info(f"Updated {credential.website} in storage")
  # now vault is updated, have to write to json file then encrypt
  #decode password to store password as string instead of bytes
  credential.decode_passwords()
  #store in json file
  store(vault_dict)

def store_new_website(credential, old_website):
  vault_dict, vault_len = get_vault_info()
  old_idx = -1
  for i in range(0, vault_len):
    account = vault_dict["credentials"][i]
    for k, v in account.items():
      if k == old_website:
        old_idx = i

  # replace old key with new key
  vault_dict["credentials"][old_idx] = credential.account
  print(vault_dict["credentials"])
  store(vault_dict)

def store_new_username(credential, previous_username, new_username):
  vault_dict, vault_len = get_vault_info()
  old_user_idx = -1
  website_idx = -1

  print(vault_dict)
  for i in range(0, vault_len):
    account_arr = vault_dict["credentials"][i][credential.website]
    for j in range(0, len(account_arr)):
      for k, v in account_arr[j].items():
        if k == previous_username:
          old_user_idx = j
          website_idx = i

  data = vault_dict["credentials"][website_idx][credential.website][old_user_idx].pop(previous_username)
  print(data)
  vault_dict["credentials"][website_idx][credential.website][old_user_idx][new_username] = data
  print(vault_dict)
  store(vault_dict)

def store(v_dict):
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, 'vault.json')
  f = open(filename, 'w')
  json.dump(v_dict, f, indent=4)
  f.close()
  #encrypt json file
  key.encrypt_vault()
  logger.info("Encrypted storage")

def get_vault_info():
  vault_str = key.decrypt_vault().decode('utf-8')
  vault_dict = json.loads(vault_str)
  vault_len = len(vault_dict["credentials"])
  return vault_dict, vault_len