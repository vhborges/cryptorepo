def xor1 (KEY1, KEY2):
    return bytes(a ^ b for a,b in zip(KEY1,KEY
2))

def xor2 (KEY, byte):
    lista = [byte for _ in range(len(KEY))]
    return bytes(a ^ b for a,b in zip(KEY, lis
ta))

