import random
from bs4 import BeautifulSoup
import requests

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

nomer_tidak_keluar = []  # Inisialisasi daftar nomor tidak keluar
angka_main_1 = []  # Inisialisasi daftar angka main 1
angka_main_2 = []  # Inisialisasi daftar angka main 2
angka_ikut = []  # Inisialisasi daftar angka ikut

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
            # Cek apakah kombinasi_str ada di daftar nomer_tidak_keluar
            if kombinasi_str not in nomer_tidak_keluar:
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

    # Tambahkan angka ikut secara acak ke dalam kombinasi
    if angka_ikut:
        kombinasi_ai = []
        for komb in kombinasi_am:
            if angka_ikut:
                ai = random.choice(angka_ikut)
                posisi = random.choice([0, 1, 2, 3])  # Posisi acak di antara dua digit pertama dan dua digit terakhir
                komb = komb[:posisi] + str(ai) + komb[posisi+1:]
            kombinasi_ai.append(komb)
        kombinasi_am = kombinasi_ai

    return kombinasi_am

text1 = "GUNAKAN TANDA BINTANG * UNTUK MEMISAHKAN ANGKA PADA AI, AM1 DAN AM2"
text2 = "AI  adalah ANGKA IKUT"
text3 = "AM1 adalah ANGKA MAIN 1100"
text4 = "AM2 adalah ANGKA MAIN 0011"

print(text1)
print(text2)
print(text3)
print(text4)

print()

def scrape_nomer_tidak_keluar():
    # URL dari halaman yang ingin di-scrape
    url = 'https://www.gaungaksara4d.com/wap'

    # Mendapatkan konten HTML dari URL
    response = requests.get(url)
    html_content = response.content

    # Parse konten HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Cari semua elemen 'a' di dalam 'li' di dalam 'ul' dengan class 'general-ul'
    ul_element = soup.find('ul', class_='locationtable general-ul')
    li_elements = ul_element.find_all('li')

    hasil_string = "ANGKA MATI: "
    nomer_tidak_keluar = []

    # Ekstrak dan simpan teks dari setiap elemen 'a' dalam elemen 'li'
    for li in li_elements:
        a_element = li.find('a')
        if a_element:
            try:
                result_text = a_element.text.split("|")[-1].strip()
                # Tambahkan hasil ke string hasil jika bukan tanda hubung (-)
                if result_text != "-":
                    hasil_string += f"{result_text} "
                    nomer_tidak_keluar.append(result_text)
            except IndexError:
                # Jika gagal mengambil teks, lewati elemen ini
                continue
    # Cetak hasil
    print(hasil_string)
    return nomer_tidak_keluar

print()

def main():
    global jumlah_kombinasi
    global nomer_tidak_keluar
    global angka_main_1
    global angka_main_2
    global angka_ikut

    # Scrape nomer tidak keluar dari website
    nomer_tidak_keluar = scrape_nomer_tidak_keluar()
    
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
    
    # Minta input angka ikut (AI)
    while True:
        try:
            ai_input = input("MASUKAN AI  : ")
            if ai_input:
                angka_ikut = [int(ai) for ai in ai_input.split("*")]
                if all(0 <= ai <= 9 for ai in angka_ikut):
                    break
                else:
                    print("Angka ikut harus antara 0 dan 9.")
            else:
                angka_ikut = []
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    # Minta input angka main 1 (AM1)
    while True:
        try:
            am1_input = input("MASUKAN AM1 : ")
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
            am2_input = input("MASUKAN AM2 : ")
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
    
    # Bet 2D tanpa duplikasi
    bet_2d_set = set()
    for kombinasi in hasil_kombinasi:
        if kombinasi[2] != kombinasi[3]:
            bet_2d_set.add(f"{kombinasi[2]}{kombinasi[3]}")
            bet_2d_set.add(f"{kombinasi[3]}{kombinasi[2]}")
    bet_2d_str = '*'.join(bet_2d_set) + f'#{bet_2d}'
    
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
