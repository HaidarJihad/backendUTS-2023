from Animal import *
class Buaya(Animal):
    def __init__(self, name, hidup, makanan, berkembang_biak, habitat, Berat):
        super().__init__(name, hidup, makanan, berkembang_biak)
        self.habitat = habitat
        self.berat = Berat
    def cetak(self):
        super().cetak()
        print(f"Habitatnya berada di {self.habitat}")
        print(f"Berat {self.berat}")
    def bernafas(self):
        print(f"{self.name} Bernafas dengan Paru-paru.")
    def merayap(self):
        print(f"{self.name} Merayap menggunakan 4 kakinya")