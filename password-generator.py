#!/bin/python3
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.-abcdefghijklmnopqrstuvwxyz'

length = input('password length? ')
length = int(length)

number_of_passwords = input('number of passwords: ')
number_of_passwords = int(number_of_passwords)

number_pf_passwords = 0
for n in range(number_of_passwords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
