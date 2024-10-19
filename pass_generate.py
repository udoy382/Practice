import random

def generate_password(length=8):
  """
  Generates a random password of the specified length using letters a-zA-Z.

  Args:
      length (int, optional): The desired length of the password. Defaults to 8.

  Returns:
      str: The generated random password.
  """
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  password = "".join(random.sample(characters, length))
  return password

# Example usage
password = generate_password()
print(password)
