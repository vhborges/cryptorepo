from random import choice
from string import ascii_lowercase, ascii_uppercase

def le_mapeamentos(filename):
    mapeamentos = {}
    with open(filename) as reader:
        for line in reader:
            cipherlinha = line.split(" ")
            for letra, cipherletra in zip(range(ord("a"), ord("z")), cipherlinha):
                if cipherletra != '-':
                    if mapeamentos.get(chr(letra)) != None:
                        mapeamentos[chr(letra)].append(cipherletra)
                    else:
                        mapeamentos[chr(letra)] = [cipherletra]
    return mapeamentos

def encripta(plaintext, mapeamentos):
    plaintext = plaintext.lower()
    ciphertext = ""
    for letra in plaintext:
        if letra in ascii_lowercase:
            ciphertext += choice(mapeamentos[letra])
        elif letra == " ":
            ciphertext += " "
    return ciphertext

def decripta(ciphertext, mapeamentos):
    plaintext = ""
    for letra in ciphertext:
        if letra == " ":
            plaintext += " "
            continue
        for cipherletra, lista in mapeamentos.items():
            if letra in lista:
                plaintext += cipherletra
    return plaintext

plaintext = input("Plaintext: ")
mapeamentos = le_mapeamentos("mapeamentos.txt")
ciphertext = encripta(plaintext, mapeamentos)
print(ciphertext)
plaintext = decripta(ciphertext, mapeamentos)
print(plaintext)
