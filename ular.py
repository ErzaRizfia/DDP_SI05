from animal import *
class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,berjenis,warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = berjenis
        self.warna = warna
    def cetak_ular(self):
        super().cetak()
        print(f'ular ini berjenis {self.jenis}dan hewan ini warnanya  {self.warna}')

piton = ular('ular piton', 'ayam', 'darat', 'bertelur','berbisa' , 'coklat')
piton.cetak_ular()      

        


        