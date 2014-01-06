#!/usr/bin/env python
# http://www.tylerlesmann.com/2008/dec/19/encrypting-database-data-django/
import binascii
import string
from random import choice
from Crypto.Cipher import AES

EOD = '`%EofD%`' # This should be something that will not occur in strings

def genstring(length=16, chars=string.printable):
    return ''.join([choice(chars) for i in range(length)])

def encrypt(key, s, iv):
    obj = AES.new(key, AES.MODE_CFB, iv)
    datalength = len(s) + len(EOD)
    if datalength < 16:
        saltlength = 16 - datalength
    else:
        saltlength = 16 - datalength % 16
    ss = ''.join([s, EOD, genstring(saltlength)])
    return binascii.b2a_base64(obj.encrypt(ss))

def decrypt(key, s, iv):
    obj = AES.new(key, AES.MODE_CFB, iv)
    ss = obj.decrypt(binascii.a2b_base64(s))
    return ss.split(EOD)[0]

if __name__ == '__main__':
    # for i in xrange(8, 20):
        # s = genstring(i)
        s = 'U2FsdGVkX19dKcS7eMVZyx0m1WL5gib1Blf7I3Le9s0Mw0Xztqouc3KpYaFrNoCm'
        key = genstring(32)
        print('The key is', key)
        print('The string is', s)
        cipher  = encrypt(key, s, 'here is an iv123')
        print('The encrypted string is', cipher)
        print('This decrypted string is', decrypt(key, cipher, 'here is an iv123'))
