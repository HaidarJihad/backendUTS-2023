class Animal:
    name = ""
    hidup = ""
    makanan = ""
    berkembang_biak = ""

    def __init__(self, name, hidup, makanan, berkembang_biak):
        self.name = name
        self.hidup = hidup
        self.makanan = makanan
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print(f"Nama : {self.name}")
        print(f"Hidup di : {self.hidup}")
        print(f"Memakan : {self.makanan}")
        print(f"Berkembang biak : {self.berkembang_biak}\n")