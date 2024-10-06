from flask import Flask, render_template, request, url_for
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

# Definisi digit global dan batas angka
nama_digit_global = {
    1: "AS",
    2: "KOP",
    3: "KEPALA",
    4: "EKOR"
}

batas_atas_global = {"AS": 9, "KOP": 9, "KEP": 9, "EKO": 9}
batas_bawah_global = {"AS": 0, "KOP": 0, "KEP": 0, "EKO": 0}

nomer_tidak_keluar = []
angka_main_1 = []
angka_main_2 = []
angka_ikut = []

# Fungsi untuk generate kombinasi
def generate_kombinasi(jumlah_kombinasi):
    kombinasi = []
    for _ in range(jumlah_kombinasi):
        while True:
            digit_acak = {}
            for nama_digit, batas_atas, batas_bawah in zip(nama_digit_global.values(), batas_atas_global.values(), batas_bawah_global.values()):
                while True:
                    angka = random.randint(batas_bawah, batas_atas)
                    if angka not in digit_acak.values():
                        digit_acak[nama_digit] = angka
                        break
            digit_urut = sorted(digit_acak.items(), key=lambda item: list(nama_digit_global.values()).index(item[0]))
            kombinasi_str = "".join(str(angka) for _, angka in digit_urut)
            if kombinasi_str not in nomer_tidak_keluar:
                kombinasi.append(kombinasi_str)
                break
    return kombinasi

# Fungsi untuk scraping nomor tidak keluar
def scrape_nomer_tidak_keluar(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        ul_element = soup.find('ul', class_='locationtable general-ul')
        li_elements = ul_element.find_all('li')

        scraped_data = []
        for li in li_elements:
            a_element = li.find('a')
            if a_element:
                result_text = a_element.text.split("|")[-1].strip()
                if result_text != "-":
                    scraped_data.append(result_text)
                    nomer_tidak_keluar.append(result_text)
        return scraped_data
    except Exception as e:
        return str(e)

# Fungsi untuk menghitung bet 2D, 3D, dan 4D
def calculate_bet(kombinasi):
    bet_4d_list = []
    bet_3d_list = []
    bet_2d_set = set()

    for komb in kombinasi:
        # Bet 4D
        bet_4d_list.append(f"{komb[0]}{komb[1]}{komb[2]}{komb[3]}")
        bet_4d_list.append(f"{komb[0]}{komb[1]}{komb[3]}{komb[2]}")

        # Bet 3D
        bet_3d_list.append(f"{komb[1]}{komb[2]}{komb[3]}")
        bet_3d_list.append(f"{komb[1]}{komb[3]}{komb[2]}")

        # Bet 2D tanpa duplikasi
        if komb[2] != komb[3]:
            bet_2d_set.add(f"{komb[2]}{komb[3]}")
            bet_2d_set.add(f"{komb[3]}{komb[2]}")

    return {
        "4D": '*'.join(bet_4d_list),
        "3D": '*'.join(bet_3d_list),
        "2D": '*'.join(bet_2d_set)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        jumlah_kombinasi = int(request.form.get('jumlah_kombinasi'))
        ai = request.form.get('ai')
        am1 = request.form.get('am1')
        am2 = request.form.get('am2')

        # Memproses input data
        angka_ikut.clear()
        angka_ikut.extend([int(ai) for ai in ai.split("*") if ai])

        angka_main_1.clear()
        angka_main_1.extend([int(am1) for am1 in am1.split("*") if am1])

        angka_main_2.clear()
        angka_main_2.extend([int(am2) for am2 in am2.split("*") if am2])

        # Scraping dan kombinasi
        hasil_scrape = scrape_nomer_tidak_keluar(url)
        hasil_kombinasi = generate_kombinasi(jumlah_kombinasi)

        # Kalkulasi bet 2D, 3D, dan 4D
        bets = calculate_bet(hasil_kombinasi)

        return render_template('index.html', scraped_data=hasil_scrape, kombinasi=hasil_kombinasi, bets=bets)

    return render_template('index.html', scraped_data=[], kombinasi=[], bets={})

if __name__ == '__main__':
    app.run(debug=True)
