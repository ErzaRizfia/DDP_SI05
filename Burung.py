from animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
     super().__init__(nama, makanan,hidup,berkembang_biak)
     self.jenis_bulu = jenis_bulu
     self.bunyi = bunyi

    def cetak_burung(self):
       super().cetak()
       print(f'hewan ini berbulu{self.jenis_bulu} dan hewan ini berbunyi{self.bunyi}')

print('---objek pertama---')       
beo = burung('burung beo','biji_bijian','udara','bertelur','blue and orange','kamu jelek')
beo.cetak_burung()
