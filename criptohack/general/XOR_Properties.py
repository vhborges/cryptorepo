def xor (KEY, byte):
    lista = [byte for _ in range(len(KEY))]
    return bytes(a ^ b for a,b in zip(KEY, lista))

cypher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for x in range(256):
    aux = xor (cypher, x)
    if b"crypto" in aux:
        print (aux)

teste = ''' asdfas
asdfasdf
sadf
'''

print(("saldfkjasdkf"
"asdfas"))
