import math

def l_persegi(sisi) :
    luas = sisi *sisi
    keliling = sisi * sisi * sisi * sisi
    print(f"Luas Persegi {sisi} x {sisi} = {luas}")
    print(f"Kelilig Persegi adalah {keliling}")

def l_persegi_panjang(panjang, lebar) :
    luas = panjang * lebar
    keliling = 2 * (panjang+lebar)
    print(f"Luas Persegi Panjang {panjang} x {lebar} = {luas}")
    print(f"Kelilig Persegi Panjang adalah {keliling}")

def l_segita(alas, tinggi) :
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga 1/2 x {alas} x {tinggi} = {luas}")

def l_lingkaran(jari1, jari2) :
    luas = 3.14 * jari1 * jari2
    print(f"Luas Lingkaran phi x {jari1} x {jari2} = {luas}")

def l_jajar_genjang(alas, tinggi) :
    luas = alas*tinggi
    print(f"Luas Jajar Genjang {alas} x {tinggi} = {luas}")
    
    
def l_kubus(sisi):
    luas = 6 * (sisi ** 2)
    print(f"Luas Kubus 6 x ({sisi} x {sisi}) = {luas}")

def l_balok(panjang, lebar, tinggi):
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"Luas Balok 2 x ({panjang} x {lebar} + {panjang} x {tinggi} + {lebar} x {tinggi}) = {luas}")

def l_tabung(jari, tinggi):
    luas = 2 * 3.14 * jari * (jari + tinggi)
    print(f"Luas Tabung 2 x phi x {jari} x ({jari} + {tinggi}) = {luas}")

def l_kerucut(jari, tinggi):
    luas = 3.14 * jari * (jari + math.sqrt((tinggi ** 2) + (jari ** 2)))
    print(f"Luas Kerucut phi x {jari} x ({jari} + √({tinggi}² + {jari}²)) = {luas}")

def l_bola(jari):
    luas = 4 * 3.14 * (jari ** 2)
    print(f"Luas Bola 4 x phi x ({jari} x {jari}) = {luas}")


