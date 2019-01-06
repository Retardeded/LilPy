from random import randint
from math import *

def remove_space(text):
  tmp = []
  to_low = 32
  for i in range(0, len(text)):
    if(ord(text[i]) != 32 ):
        if(ord(text[i]) <= 90):
            letter = chr(ord(text[i]) + to_low)
            tmp.append(letter)
        else:
            tmp.append(text[i])

  return tmp

def encrypt_cezar(text, value):
  for i in range(0, len(text)):
    letter_encoded = ord(text[i])
    letter_encoded = 97 + (letter_encoded-97 + value ) % 26
    text[i] = chr(letter_encoded)

def decrypt_cezar(text, value):
  for i in range(0, len(text)):
    letter_encoded = ord(text[i])
    letter_encoded = 97 + (letter_encoded-97 - value) % 26
    text[i] = chr(letter_encoded)

text = "TEKST do zaszyfrowania"
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_chars = []
for i in range(0, len(alphabet_chars)):
  alphabet_chars.insert(0, alphabet[i])

chars = []
for i in range(0, len(text)):
  chars.append(text[i])

value_to_sub = 97
random_value = 2

print(chars)
chars = remove_space(chars)
print(chars)
encrypt_cezar(chars, random_value)
print(chars)
decrypt_cezar(chars, random_value)
print(chars)