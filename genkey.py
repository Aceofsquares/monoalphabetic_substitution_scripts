#!/usr/bin/python

from string import ascii_uppercase as upper
from random import sample

'''
Quickly generates a monoalphabetic key used
to map one letter to another letter.  The
mapping can end up being to itself.  For instance
if the program printed YWUPFNMCBQOTEDRGASLZJVIXHK then
the mapping would be

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
| | | | | | | | | | | | | | | | | | | | | | | | | |
Y W U P F N M C B Q O T E D R G A S L Z J V I X H K

where A maps to Y, B maps to W, etc.
'''

print ''.join(sample(upper, len(upper)))
