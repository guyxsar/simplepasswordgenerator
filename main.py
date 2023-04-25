import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

oneHalfAlphabet = letters + digits
twoHalfAlphabet = special_chars + special_chars
alphabet = oneHalfAlphabet + twoHalfAlphabet

pwd_length = 24


pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)
