import os

def vault_exists():
  """
  Checks if the user has a stored vault
  """
  a = os.path.exists('vault.json')
  return a