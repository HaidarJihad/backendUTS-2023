# membuat class mobil
class mobil: 

    def __init__(self, tipe, roda, kecepatan, warna):
        self.time = tipe
        self.roda = roda
        self.kecepatan = kecepatan
        self.warna = warna

    def maju(self):
        print("Maju dengan kecepatan", self.kecepatan, "km/jam")

    def klakson(self):
        print("klakson")

    def belok(self, arah):
        print("Belok arah", arah)

    def warna(self, warna):
        print("Warna mobil", warna)

# membuat object
mobil1 = mobil("Avanza", 4, 60, "putih")
print("warna mobil: ", mobil1.warna)

# memanggil fungsi dalam class mobil
mobil1.maju()
mobil1.klakson()
mobil1.belok("kiri")
