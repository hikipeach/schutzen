import json
import bcrypt
import logging

from src.key import decrypt_vault

logger = logging.getLogger(__name__)

def login():
    """
    Logs the user in by comparing their entered password to their hashed password
    """
    MAX_ATTEMPT = 3
    current_attempt = 1
    logged_in = False
    while current_attempt <= MAX_ATTEMPT and not logged_in:
        entered, master = get_hashed_passwords()
        if is_verified(entered, master):
            logger.info("User successfully verified their master password.")
            print("verification successful.")
        else:
            logger.info("User unsuccessfully verified their master password.")
            print("verification unsuccessful.")
            print(f"attempts left {MAX_ATTEMPT - current_attempt}")
            current_attempt += 1
            logged_in = False
    logger.error("User reached maximum attemps for logging in. Program will now close.")
    raise Exception("reached maximum attempts for logging in")

def is_verified(hashed_entered_password: bytes, hashed_master_password: bytes):
    """
    Verifies the user based on the hash of the password they entered and the hash of the master password
    """
    logger.info("Verifying user's master password...")
    return hashed_entered_password == hashed_master_password

def get_hashed_passwords():
    entered_password = input("enter your master password: ")
    # get the data from the json file
    vault = decrypt_vault().decode('utf-8')
    logger.info("Vault decrypted.")
    data = json.loads(vault)
    # encode salt and master password to utf-8
    salt = data["salt"].encode('utf-8')
    hashed_master_password = data["hashed_password"].encode('utf-8')
    logger.info("Salt and master password encoded.")
    # hash the entered password with the salt
    entered_password_bytes = entered_password.encode('utf-8')
    logger.info("Entered password encoded.")
    hashed_entered_password = bcrypt.hashpw(entered_password_bytes, salt)
    logger.info("Entered password hashed.")
    return hashed_entered_password, hashed_master_password

