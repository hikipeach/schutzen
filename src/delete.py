import os
from login import get_hashed_passwords
from utility import vault_exists

def delete():
  if not vault_exists():
    print("error: the vault you are trying to delete does not exist.")
  else:
    print("are you sure you would like to delete your vault?")
    response = input("press 'y' for yes, or any other key for no: ").lower()
    if response != 'y':
      print('no changes to vault made.')
    else:
      print("verify your master password.")
      entered, master = get_hashed_passwords()
      if entered == master:
        os.remove('vault.json')
        os.remove('../config/key.env')
        print('vault removed.')
      else:
          print('error: unable to delete vault due to incorrect master password')