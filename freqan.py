#!/usr/bin/python

from collections import Counter
from re import sub
from argparse import ArgumentParser, FileType

"""
Performs basic frequency analysis of a given text.
Call by either of the following methods

python freqan.py [options] file

or if you chmod +x this file you can simply

freqan.py [options] file

Results are displayed as capitalized characters and
a value that represents the number of times they appear
in the text.

options
-c, --chunk-size N This will split the lines into chunks
                   of size N and return the count of the chunks.

-t, --top N	   This will return the top N most common
		   results.

"""

parser = ArgumentParser('Perform frequency analysis of given text')

parser.add_argument('filename', type=FileType('r'), help='File to be analyzed')
parser.add_argument('-c', '--chunk-size', type=int, default=1, nargs='?', help='Size of chunks.')
parser.add_argument('-t', '--top', type=int, default=-1, nargs='?', help='Return the top n most common. Default: All')

args = parser.parse_args()

with args.filename as infile:
    c = Counter()
    chunk_size = args.chunk_size
    for line in infile:
        line = line.upper()
        line = sub('[^A-Z0-9]', '', line)
        for i in range(0, len(line)-(chunk_size-1)):
            chunk = tuple([line[i:i+chunk_size]])
            c.update(chunk)
    for com in c.most_common(None if args.top <= 0 else args.top):
        print "{} -> {}".format(com[0], com[1])
