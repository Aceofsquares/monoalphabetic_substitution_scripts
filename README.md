# Monoalphabetic Substitution Scripts

These scripts are used to do some basic monoalphabetic substitution stuff.  This only applies to English characters.

**freqan.py** \- Performs frequency analysis on given text.  The default of this script is to do frequency analysis on
                individual letters.  You can do analysis on chunks to determine common trigrams for example by issuing
                -c or --chunk-size and an N for the size.  The output for these might cause the terminal to over buffer so
                you can either output to a file by piping to a file or you can use -t or --top to get the top N most common. <br />
                
                Example Usages: 
                python freqan.py file.txt
                python freqan.py -c 3 file.txt
                
**monosub.py** \- Allows you to encrypt or decrypt based on a given key (alphabet).  This script requires 3 positional arguments
                 which are as follows. <br />
                 1. _mode_     \- This argument tells the script whether to encrypt or decrypt.  Pass either encrypt, enc, decrypt,
                 or dec as the mode. <br />
                 2. _key_      \-  The key is the alphabetic cipher to use for encryption and decryption.<br />
                 3. _filename_ \- The file to encrypt or decrypt using the key.  You can use hyphen for stdin and CTRL-D (twice)
                 to end the input. <br >
                 
                 Example Usages:
                 python monosub.py enc JGVKMYXTPFNWUDEQBRCLZSAIHO plain.txt > encrypted.txt
                 python monosub.py decrypt JGVKMYXTPFNWUDEQBRCLZSAIHO encrypted.txt > decrypted.txt
                 
**genkey.py** \- If you want to generate a random key for a monoalphabetic substitution cipher, simply run this script.
                  
                  Example Usage:
                  python genkey.py
                  
For fun, find some text and put it into a file.  Then run

  `python monosub.py enc $(python genkey.py) plain.txt`
  
Then try to figure out the key that was generated.
