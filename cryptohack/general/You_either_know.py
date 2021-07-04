from xor import *
from string import ascii_lowercase, ascii_uppercase

cypher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print (len(cypher))

# crib = b"crypto{"
# key = xor1 (crib, cypher)

key = b'myXORkey'
crib = xor1 (key, cypher)

flag = b'crypto{1bU'

print (crib)
