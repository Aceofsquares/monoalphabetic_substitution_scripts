#!/usr/bin/python

from sys import exit
from argparse import ArgumentParser, FileType
from string import ascii_uppercase as upper

'''
This program will encrypt plaintext using
monoalphabetic substitution encrypted text 
using the provided key.  Key must be
26 characters where the first character maps to A, 
second to B, third to C, etc. 
'''

def crypt(alpha1, alpha2):
    mapping = dict()
    for (d, e) in zip(alpha1, alpha2):
   	mapping[d] = e
    return mapping

parser = ArgumentParser('Encrypts text using monoalphabetic substitution')

parser.add_argument('mode', help='Determines whether to encrypt (enc) or decrypt (dec)')
parser.add_argument('key', help='Key to use to encrypt the given text')
parser.add_argument('filename', type=FileType('r'), help='File to be encrypted')

args = parser.parse_args()

mode = args.mode
key = args.key

result_text = ''

conversion = None

if len(key) < 26 or len(key) > 26:
    print "Key must be 26 characters"
    exit(1)

if mode in ['enc', 'encrypt']:
    conversion = crypt(upper, key)
elif mode in ['dec', 'decrypt']:
    conversion = crypt(key, upper)
else:
    print "Mode must be either encrypt (enc) or decrypt (dec)"
    exit(2)

with args.filename as infile:
    for line in infile:
        line = line.upper()
        for c in line:
            result_text += conversion.get(c, c)

print result_text
