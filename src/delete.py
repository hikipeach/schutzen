import os
import logging
from login import get_hashed_passwords
from utility import vault_exists

logger = logging.getLogger(__name__)
logging.basicConfig(filename="schutzen.log", filemode="utf-8", level=logging.ERROR, format='%(levelname)s:%(message)s %(asctime)s', datefmt='%m/%d/%Y %I:%M:%S %P')

def delete():
  """
  Deletes a valid valid
  """
  if not vault_exists():
    logger.error("User tried to delete a vault that does not exist.")
    raise Exception("vault does not exist.")
  else:
    print("are you sure you would like to delete your vault?")
    response = input("press 'y' for yes, or any other key for no: ").lower()

    if response != 'y':
      logger.info("User chose not to delete vault.")
      print('no changes to vault made.')
    else:
      logger.info("Verifying master password...")
      print("verify your master password.")
      entered, master = get_hashed_passwords()

      if entered == master:
        logger.info("Verifying master password is successful.")
        os.remove('vault.json')
        os.remove('../config/key.env')
        print('vault removed.')
        logger.info("User deleted vault.")
      else:
        logger.error("Unable to delete vault due to incorrect master password.")
        print('error: unable to delete vault')