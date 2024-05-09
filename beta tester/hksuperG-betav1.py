import random

def generate_number(digit):
    # Menghasilkan nomor acak dengan panjang digit yang diberikan
    return '{:0{}}'.format(random.randint(0, 10**digit-1), digit)

# Menghasilkan 30 nomor dengan panjang 2, 3, dan 4 digit secara bersamaan dan memisahkan dengan simbol # dan +
for _ in range(20):
    nomor_4d = generate_number(4)
    ribuan = nomor_4d[1:]
    nomor_3d = ribuan
    nomor_2d = ribuan[1:]
    print(nomor_4d + "#200", nomor_3d + '#300', nomor_2d + '#400', sep='+', end='+')

