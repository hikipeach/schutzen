import base64
import json
import bcrypt

def login():
    """
    Logs the user in by comparing their entered password to their hashed password
    """
    MAX_ATTEMPT = 3
    current_attempt = 1
    logged_in = False
    while current_attempt <= MAX_ATTEMPT and not logged_in:
        entered_password = input("enter your master password: ")
        # get the data from the json file
        with open('vault.json', 'r') as f:
            data = json.load(f)
        print(data)
        # encode salt and master password to utf-8
        salt = data["salt"].encode('utf-8')
        hashed_master_password = data["hashed_password"].encode('utf-8')
        # hash the entered password with the salt
        entered_password_bytes = entered_password.encode('utf-8')
        hashed_entered_password = bcrypt.hashpw(entered_password_bytes, salt)
        if is_verified(hashed_entered_password, hashed_master_password):
            print("successfully logged in.")
            logged_in = True
        else:
            print("login unsuccessful.")
            print(f"attempts left {MAX_ATTEMPT - current_attempt}")
            current_attempt += 1

def is_verified(hashed_entered_password: bytes, hashed_master_password: bytes):
    """
    Verifies the user based on the hash of the password they entered and the hash of the master password
    """
    return hashed_entered_password == hashed_master_password


login()