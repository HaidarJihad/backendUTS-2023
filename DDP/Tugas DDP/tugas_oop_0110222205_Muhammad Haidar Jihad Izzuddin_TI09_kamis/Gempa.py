class Gempa():
    lokasi = ''
    skala = ''

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("="*50)
            print(f"Lokasi Gempa berada di {self.lokasi}\nDengan Skala {self.skala} = Dampak gempa tidak mengakibatkan apa-apa.")
            print("="*50)
        elif self.skala >= 2 and self.skala < 4:
            print("="*50)
            print(f"Lokasi Gempa berada di {self.lokasi}\nDengan Skala {self.skala} = Dampak gempa mengakibatkan retak pada bangunan.")
            print("="*50)
        elif self.skala >= 2 and self.skala < 6:
            print("="*50)
            print(f"Lokasi Gempa berada di {self.lokasi}\nDengan Skala {self.skala} = Dampak gempa mengakibatkan bangunan roboh.")
            print("="*50)
        else:
            print("="*50)
            print(f"Lokasi Gempa berada di {self.lokasi}\nDengan Skala {self.skala} = Dampak gempa mengakibatkan bangunan roboh dan berpotensi tsunami.")
            print("="*50)