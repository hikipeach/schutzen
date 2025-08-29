class Credential:
  """Represents the credentials the user would like to store for a given website"""
  def __init__(self, website, username, password):
    self.website = website
    self.account = {website: [{username: password}]}

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
          password = 'a'
          confirmed_password = 'b'
          while password != confirmed_password:
              account_list = self.account[self.website]
              username = input(f"enter your username for {self.website}: ")
              password = input(f"enter your password for {self.website}: ")
              confirmed_password = input(f"confirm your password for {self.website}: ")
              if password != confirmed_password:
                  print("error: passwords do not match")
              else:
                credential = {username: password}
                account_list.append(credential)
                print(f"added account {username} for {self.website}")

  def change_website(self, website):
      if self.website != website:
          print("error: website not found")
      else:
          old_credential = self.account.pop(self.website)
          new_website = input("enter the new website url: ")
          self.website = new_website
          self.account[self.website] = old_credential
          print(f"previous website '{website}' has been changed to '{new_website}'")

  def find_username(self, username: str):
      account_list = self.account[self.website]
      for i in range(0, len(account_list)):
          for k, v in account_list[i].items():
              if username == k:
                  return i
          else:
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
          print(f"username changed to {new_username}")

  def change_password(self, username, new_password):
      username_idx = self.find_username(username)
      if username_idx == -1:
          print("username not found.")
      else:
          self.account[self.website][username_idx][username] = new_password
          print(f"password changed to {new_password}.")