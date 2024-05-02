import random

# Daftar angka mati (tidak boleh muncul)
angka_mati = [1, 2, 3, 4]  # Ubah sesuai kebutuhan

# Nama digit
nama_digit_global = {
    1: "AS",
    2: "KOP",
    3: "KEP",
    4: "EKO"
}

# Jumlah kombinasi yang ingin dihasilkan
jumlah_kombinasi = 2  # Ubah sesuai kebutuhan

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


def generate_kombinasi():
    kombinasi = []
    for _ in range(jumlah_kombinasi):
        # Buat kamus untuk menyimpan digit acak
        digit_acak = {}
        for nama_digit, batas_atas, batas_bawah in zip(nama_digit_global.values(), batas_atas_global.values(), batas_bawah_global.values()):
            while True:
                # Generate angka acak
                angka = random.randint(batas_bawah, batas_atas)

                # Pastikan angka tidak termasuk dalam angka mati dan belum digunakan sebelumnya
                if angka not in angka_mati and angka not in digit_acak.values():
                    digit_acak[nama_digit] = angka
                    break

        # Urutkan digit berdasarkan nama
        digit_urut = sorted(digit_acak.items(), key=lambda item: list(nama_digit_global.values()).index(item[0]))

        # Buat string kombinasi
        kombinasi_str = ""
        for nama_digit, angka in digit_urut:
            kombinasi_str += f"{angka}{nama_digit}"

        kombinasi.append(kombinasi_str)
    return kombinasi


# Hasil kombinasi
hasil_kombinasi = generate_kombinasi()

# Cetak hasil
print("HASIL KOMBINASI:")
for kombinasi in hasil_kombinasi:
    print(kombinasi)

# Hitung bet
bet_4d = 0
bet_3d = 0
bet_2d = 0

for kombinasi in hasil_kombinasi:
    # Pisahkan angka dan nama digit
    digit_angka = [int(karakter) for karakter in kombinasi if karakter.isdigit()]
    digit_nama = [karakter for karakter in kombinasi if not karakter.isdigit()]

    # Bet 4D
    bet_4d_str = f"{digit_angka[0]}{digit_angka[1]}{digit_angka[2]}{digit_angka[3]}*"
    bet_4d_str += f"{digit_angka[0]}{digit_angka[1]}{digit_angka[2]}{digit_angka[3]}"
    bet_4d += 300

    # Bet 3D
    for i in range(4):
        bet_3d_str = f"{digit_angka[i]}{digit_angka[(i+1) % 4]}{digit_angka[(i+2) % 4]}*"
        bet_3d_str += f"{digit_angka[i]}{digit_angka[(i+1) % 4]}{digit_angka[(i+2) % 4]}"
        bet_3d += 400

    # Bet 2D
    for i in range(4):
        for j in range(i+1, 4):
            bet_2d_str = f"{digit_angka[i]}{digit_angka[j]}*"
            bet_2d_str += f"{digit_angka[i]}{digit_angka[j]}"
            bet_2d += 500

    # Cetak bet
    print(f"BET 4D: {bet_4d_str}#{bet_4d}")
    print(f"BET 3D: {bet_3d_str}#{bet_3d}")
    print(f"BET 2D: {bet_2d_str}#{bet_2d}")
    print()

    # Reset bet
    bet_4d = 0
    bet_3d = 0
    bet_2d = 0
