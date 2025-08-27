import json
import bcrypt
from key import decrypt_vault

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
            print("verification successful.")
            return True
        else:
            print("verification unsuccessful.")
            print(f"attempts left {MAX_ATTEMPT - current_attempt}")
            current_attempt += 1
            logged_in = False
    return False

def is_verified(hashed_entered_password: bytes, hashed_master_password: bytes):
    """
    Verifies the user based on the hash of the password they entered and the hash of the master password
    """
    return hashed_entered_password == hashed_master_password

def get_hashed_passwords():
    entered_password = input("enter your master password: ")
    # get the data from the json file
    vault = decrypt_vault().decode('utf-8')
    data = json.loads(vault)
    # encode salt and master password to utf-8
    salt = data["salt"].encode('utf-8')
    hashed_master_password = data["hashed_password"].encode('utf-8')
    # hash the entered password with the salt
    entered_password_bytes = entered_password.encode('utf-8')
    hashed_entered_password = bcrypt.hashpw(entered_password_bytes, salt)
    return hashed_entered_password, hashed_master_password

