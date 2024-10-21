import random

print("Your Password:")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$_-.%/^()[]{}'

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)