# our alphabet starts at
g_start = ord('a')
# and it ends at
g_end = ord('z')
# so that we have end - start letters in between, + 1
g_size = g_end - g_start + 1

# shifts letters by i places (with wrap)
# TODO: add support for uppercase
def shift(c, i):
    return chr((ord(c) - g_start + i) % g_size + g_start)

def get_permutations(ciphertext):
    for i in range(g_size):
        string = ''
        for j in ciphertext.lower():
            if j == ' ':
                string += ' '
                continue
            string += shift(j, i)

        print(f'encryption key: {g_size - i}')
        print(string.upper())

if __name__ == '__main__':
    import sys

    # can use any ciphertext
    # i.e.: 'YWRA PAJJEO EJPK EJRAOP'
    if len(sys.argv) > 1:
        ciphertext = sys.argv[1]
    else:
        ciphertext = 'YWRA PAJJEO EJPK EJRAOP'

    get_permutations(ciphertext)

