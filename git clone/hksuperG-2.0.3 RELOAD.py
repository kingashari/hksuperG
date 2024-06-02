import random

# Nama digit
nama_digit_global = {
    1: "AS",
    2: "KOP",
    3: "KEPALA",
    4: "EKOR"
}

# Jumlah kombinasi yang ingin dihasilkan
jumlah_kombinasi = 0  # Inisialisasi dengan 0

# Batas atas dan bawah untuk setiap digit
batas_atas_global = {
    "AS": 9,  # Ubah sesuai kebutuhan
    "KOP": 9,  # Ubah sesuai kebutuhan
    "KEP": 9,  # Ubah sesuai kebutuhan
    "EKO": 9,  # Ubah sesuai kebutuhan
}
batas_bawah_global = {
    "AS": 0,  # Ubah sesuai kebutuhan
    "KOP": 0,  # Ubah sesuai kebutuhan
    "KEP": 0,  # Ubah sesuai kebutuhan
    "EKO": 0,  # Ubah sesuai kebutuhan
}

angka_main_1 = []  # Inisialisasi daftar angka main 1
angka_main_2 = []  # Inisialisasi daftar angka main 2

def generate_kombinasi():
    global jumlah_kombinasi
    kombinasi = []
    for _ in range(jumlah_kombinasi):
        while True:
            # Buat kamus untuk menyimpan digit acak
            digit_acak = {}
            for nama_digit, batas_atas, batas_bawah in zip(nama_digit_global.values(), batas_atas_global.values(), batas_bawah_global.values()):
                while True:
                    # Generate angka acak
                    angka = random.randint(batas_bawah, batas_atas)
                    if angka not in digit_acak.values():
                        digit_acak[nama_digit] = angka
                        break
            # Urutkan digit berdasarkan nama
            digit_urut = sorted(digit_acak.items(), key=lambda item: list(nama_digit_global.values()).index(item[0]))
            # Buat string kombinasi tanpa label
            kombinasi_str = ""
            for _, angka in digit_urut:
                kombinasi_str += f"{angka}"
            kombinasi.append(kombinasi_str)
            break

    # Terapkan angka main 1 ke dua digit pertama dan angka main 2 ke dua digit terakhir dari setiap kombinasi
    kombinasi_am = []
    for komb in kombinasi:
        if angka_main_1:
            am1, am2 = random.sample(angka_main_1, 2) if len(angka_main_1) > 1 else (angka_main_1[0], angka_main_1[0])
            komb = str(am1) + str(am2) + komb[2:]
        if angka_main_2:
            am3, am4 = random.sample(angka_main_2, 2) if len(angka_main_2) > 1 else (angka_main_2[0], angka_main_2[0])
            komb = komb[:2] + str(am3) + str(am4)
        kombinasi_am.append(komb)

    return kombinasi_am

def main():
    global jumlah_kombinasi
    global angka_main_1
    global angka_main_2
    
    # Minta input jumlah kombinasi
    while True:
        try:
            jumlah_kombinasi = int(input("MASUKAN BERAPA KOMBINASI YANG INGIN KELUAR: "))
            if jumlah_kombinasi > 0:
                break
            else:
                print("Jumlah kombinasi harus lebih dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    # Minta input angka main 1 (AM1)
    while True:
        try:
            am1_input = input("MASUKAN AM1 (pisahkan dengan bintang jika lebih dari satu, kosongkan jika tidak ada): ")
            if am1_input:
                angka_main_1 = [int(am) for am in am1_input.split("*")]
                if all(0 <= am <= 9 for am in angka_main_1):
                    break
                else:
                    print("Angka main harus antara 0 dan 9.")
            else:
                angka_main_1 = []
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    # Minta input angka main 2 (AM2)
    while True:
        try:
            am2_input = input("MASUKAN AM2 (pisahkan dengan bintang jika lebih dari satu, kosongkan jika tidak ada): ")
            if am2_input:
                angka_main_2 = [int(am) for am in am2_input.split("*")]
                if all(0 <= am <= 9 for am in angka_main_2):
                    break
                else:
                    print("Angka main harus antara 0 dan 9.")
            else:
                angka_main_2 = []
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    # Minta input betting untuk 4D, 3D, dan 2D
    while True:
        try:
            bet_4d = int(input("MASUKAN BET 4D: "))
            bet_3d = int(input("MASUKAN BET 3D: "))
            bet_2d = int(input("MASUKAN BET 2D: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    # Generate kombinasi
    hasil_kombinasi = generate_kombinasi()
    
    # Cetak hasil kombinasi
    print("\nHASIL KOMBINASI:")
    for kombinasi in hasil_kombinasi:
        print(kombinasi)
    
    # Bet 4D
    bet_4d_list = []
    for kombinasi in hasil_kombinasi:
        bet_4d_list.append(f"{kombinasi[0]}{kombinasi[1]}{kombinasi[2]}{kombinasi[3]}")
        bet_4d_list.append(f"{kombinasi[0]}{kombinasi[1]}{kombinasi[3]}{kombinasi[2]}")
    bet_4d_str = '*'.join(bet_4d_list) + f'#{bet_4d}+'
    
    # Bet 3D
    bet_3d_list = []
    for kombinasi in hasil_kombinasi:
        bet_3d_list.append(f"{kombinasi[1]}{kombinasi[2]}{kombinasi[3]}")
        bet_3d_list.append(f"{kombinasi[1]}{kombinasi[3]}{kombinasi[2]}")
    bet_3d_str = '*'.join(bet_3d_list) + f'#{bet_3d}+'
    
    # Bet 2D
    bet_2d_list = []
    for kombinasi in hasil_kombinasi:
        if kombinasi[2] != kombinasi[3]:
            bet_2d_list.append(f"{kombinasi[2]}{kombinasi[3]}")
            bet_2d_list.append(f"{kombinasi[3]}{kombinasi[2]}")
    bet_2d_str = '*'.join(bet_2d_list) + f'#{bet_2d}'
    
    hasil_taruhan = bet_4d_str + bet_3d_str + bet_2d_str
    
    # Cetak bet 4D, 3D, dan 2D
    print(f"\n4D: {bet_4d_str}")
    print(f"\n3D: {bet_3d_str}")
    print(f"\n2D: {bet_2d_str}")
    print(f"\nHASIL: {hasil_taruhan}")

if __name__ == "__main__":
    main()

text = """
...
"""
print(text)

input("Press Enter to exit...")
