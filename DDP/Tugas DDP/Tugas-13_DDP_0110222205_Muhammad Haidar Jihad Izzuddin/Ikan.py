from Animal import *
class Ikan(Animal):
    def __init__(self, name, hidup, makanan, berkembang_biak, habitat, panjang):
        super().__init__(name, hidup, makanan, berkembang_biak)
        self.habitat = habitat
        self.panjang = panjang
    def cetak(self):
        super().cetak()
        print(f"Habitatnya berada di {self.habitat}")
        print(f"Panjang {self.panjang}")
    def bernafas(self):
        print(f"{self.name} Bernafas dengan Insang.")
    def berenang(self):
        print(f"{self.name} Berenang dengan Menggerakkan ekornya")
