from Animal import *
class Gajah(Animal):
    def __init__(self, name, hidup, makanan, berkembang_biak, habitat, berat):
        super().__init__(name, hidup, makanan, berkembang_biak)
        self.habitat = habitat
        self.berat = berat
    def cetak(self):
        super().cetak()
        print(f"Habitatnya berada di {self.habitat}")
        print(f"Berat {self.berat}")
    def bernafas(self):
        print(f"{self.name} Bernafas dengan Paru-paru.")
    def karakteristik(self):
        print(f"{self.name} Termasuk kedalam hewan Herbivora")