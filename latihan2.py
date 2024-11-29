import latihan1

print('--------gunakan modul-----------')
latihan1.tambah(5,2)
latihan1.kurang(10,3)
latihan1.kali(5,6)

print('\n--gunakan modul yg ada dgn alias--')
latihan1.bagi(20,2)
latihan1.pangkat(2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from latihan1 import tambah,kurang
tambah(20,30)
kurang(2,3)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from latihan1 import*
tambah(20,30)
kurang(2,3)
kali(5,6)
bagi(20,2)
pangkat(2,3)