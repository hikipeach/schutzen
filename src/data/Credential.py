class Credential:
  """Represents the credentials the user would like to store for a given website"""
  def __init__(self, website, username, password):
    self.website = website
    self.account = {website: [{username: password}]}

  def to_string(self) -> str:
     """
     Displays the account details
     """
     account_list = self.account[self.website]
     for i in range(0, len(account_list)):
         for k, v in account_list[i].items():
             print(f"website: {self.website}")
             print(f"username: {k}\npassword: {v}\n")

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
          print(f"website '{website}' has been changed to '{new_website}'")

"""
  def change_username(self, username):
      account_list = self.account[self.website]
      #find the index of the key that matches username
"""

x = Credential('google.com', 'joe@gmail.com', 'joe1234')
x.to_string()
x.change_website('google.com')
x.to_string()