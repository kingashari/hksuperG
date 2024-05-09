import random

def generate_number(digit, avoid_list=None):
    if avoid_list is None:
        avoid_list = []
    # Menghasilkan nomor acak dengan panjang digit yang diberikan
    number = '{:0{}}'.format(random.randint(0, 10**digit-1), digit)
    while number in avoid_list:
        number = '{:0{}}'.format(random.randint(0, 10**digit-1), digit)
    return number

# Menghasilkan 20 nomor dengan panjang 2, 3, dan 4 digit secara bersamaan dan memisahkan dengan simbol # dan +
avoid_list = []
for _ in range(1):
    nomor_4d = generate_number(4, avoid_list)
    ribuan = nomor_4d[1:]
    nomor_3d = generate_number(3, avoid_list)
    nomor_2d = generate_number(7, avoid_list)
    print(nomor_4d + "#200", nomor_3d + '#300', nomor_2d + '#400', sep='+', end='')
    avoid_list.extend([nomor_4d, ribuan, nomor_3d, nomor_2d])

# Tambahkan baris kosong di akhir agar hasil cetakan tidak tampak berdesakan
print()
