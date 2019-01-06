from random import randint

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

def encrypt_random(text, alphabet_chars):
    n = len(text)
    for i in range(n):
        letter_value = ord(text[i])-97
        text[i] = alphabet_chars[letter_value]

def decrypt_random(text, key, alphabet):
    n = len(text)
    for i in range(n):
        letter_value = ord(text[i]) - 97
        text[i] = alphabet[key[letter_value]]

text = "TEKST do zaszyfrowania"
alphabet = "abcdefghijklmnopqrstuvwxyz"

used_values = []
n = len(alphabet)
print(n)
for i in range(0, n):
    used_values.append(i)
for i in range(0, n*10):
    random_1 = randint(0, n-1)
    random_2 = randint(0, n-1)
    tmp = used_values[random_1]
    used_values[random_1] = used_values[random_2]
    used_values[random_2] = tmp


alphabet_chars = [0]*n
for i in range(0, n):
  alphabet_chars[used_values[i]] = alphabet[i]

chars = []
for i in range(0, len(text)):
  chars.append(text[i])

key = [0]*n
for i in range(0, n):
    key[ord(alphabet_chars[i])-97] = i
print(used_values)
print(alphabet_chars)

print(chars)
chars = remove_space(chars)
print(chars)
encrypt_random(chars, alphabet_chars)
print(chars)
decrypt_random(chars, key, alphabet)
print(chars)