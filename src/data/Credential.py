import logging
from src import utility

logger = logging.getLogger(__name__)

class Credential:
  """Represents the credentials the user would like to store for a given website"""
  def __init__(self, website, username, password):
    encrypted_password = utility.encrypt_password(password)
    self.website = website
    self.account = {website: [{username: encrypted_password}]}
    utility.store_credential(self)

  def to_string(self) -> str:
     """
     Displays the account details
     """
     credential_string = ""
     account_list = self.account[self.website]
     for i in range(0, len(account_list)):
         for k, v in account_list[i].items():
             credential_string += f"website: {self.website}\n"
             credential_string += f"username: {k}\npassword: {v}\n"
     return credential_string

  def add_account(self, website):
      """Adds an account to existing website"""
      if website != self.website:
          print("error: website not found")
      else:
        account_list = self.account[self.website]
        username = input(f"enter your username for {self.website}: ")
        password = input(f"enter your password for {self.website}: ")
        confirmed_password = input(f"confirm your password for {self.website}: ")
        if password != confirmed_password:
          print("error: passwords do not match")
        else:
          encrypted_password = utility.encrypt_password(password)
          credential = {username: encrypted_password}
          account_list.append(credential)
          print(f"added account {username} for {self.website}")
          utility.store_credential(self)

  def change_website(self, website):
      if self.website != website:
          print("error: website not found")
      else:
          old_credential = self.account.pop(self.website)
          new_website = input("enter the new website url: ")
          self.website = new_website
          self.account[self.website] = old_credential
          print(f"previous website '{website}' has been changed to '{new_website}'")
          utility.store_new_website(self, website)

  def find_username(self, username: str):
      account_list = self.account[self.website]
      for i in range(0, len(account_list)):
          for k, v in account_list[i].items():
              if username == k:
                  return i
      return -1

  def change_username(self, previous_username, new_username):
      """
      Changes a previous username to a new username
      """
      username_idx = self.find_username(previous_username)
      if username_idx == -1:
          print("username not found.")
      else:
          account = self.account[self.website][username_idx].pop(previous_username)
          self.account[self.website][username_idx][new_username] = account
          utility.store_new_username(self, previous_username, new_username)
          print(f"username changed to {new_username}")

  def change_password(self, username, new_password):
      username_idx = self.find_username(username)
      if username_idx == -1:
          print("error: username not found.")
      else:
          confirmed_password = input("confirm your new password: ")
          if confirmed_password == new_password:
              encrypted_password = utility.encrypt_password(new_password)
              self.account[self.website][username_idx][username] = encrypted_password
              print(f"password changed.")
          else:
              print("error: unable to change password. passwords do not match.")

  def get_password(self, username):
      """displays password for a valid username"""
      username_idx = self.find_username(username)
      if username_idx == -1:
          logger.info("Unable to find username.")
          return ''
      else:
          password = self.account[self.website][username_idx][username]
          decrypted_password = utility.decrypt_password(password)
          return decrypted_password

  def display_password(self, username):
      if self.get_password(username) == '':
          print("username {username} does not exist.")
      else:
          print(f"password for {username} is {self.get_password(username)}")

  def delete_account(self, username):
      username_idx = self.find_username(username)
      if username_idx == -1:
          print("error: username does not exist")
      else:
        del self.account[self.website][username_idx]
        logger.info(f"User deleted an account associated with website: {self.website}")
        print(f"account with the username {username} been deleted.")

  def clear_accounts(self, website):
      """
      Deletes all accounts associated with a website
      """
      if website != self.website:
          print("error: invalid website")
      else:
          print("warning: this deletes all your accounts associated with the website")
          confirm_delete = input("are you sure you want to delete them? for yes enter 'y' or any other key for no: ").lower()
          if confirm_delete != 'y':
              print(f"no changes made to {website}")
          else:
            print(self.account[self.website])
            self.account[self.website].clear()
            logger.info(f"User deleted all accounts associated with {self.website}")
            print(f"all accounts have been deleted for {website}")

  def decode_passwords(self):
    for k, v in self.account.items():
          arr = self.account[k]
          for i in range(0, len(arr)):
              account = self.account[k][i]
              for u, p in account.items():
                if type(p) == bytes:
                    self.account[k][i][u] = p.decode('utf-8')
    logger.info("Decoded passwords to utf-8 for JSON storage")

