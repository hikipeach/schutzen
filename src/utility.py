import os
import pyperclip3
import asyncio

from cryptography.fernet import Fernet
from src import key

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