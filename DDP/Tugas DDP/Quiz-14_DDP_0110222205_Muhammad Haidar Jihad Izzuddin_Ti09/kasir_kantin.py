class kantin:
    def __init__(self):
        self.menu_makanan = {
        'Nasi Goreng' : 10000,
        'Piscok' : 2000,
        'Kue Sus mini' : 3000,
        'Martabak' : 8000,
        'Makaroni' : 5000
    }
        self.menu_minuman = {
        'Es Teh Manis' : 3000,
        'Teh Anget' : 2000,
        'Kopi' : 5000,
        'Susu' : 5000,
        'Jeruk Anget' : 4000
    }

    def cetak_struk(self, nama, uang, pesanan):
        total_harga = 0
        for p in pesanan:
            total_harga += p['harga']
        print(f'Nama: {nama}')
        print('Pesanan: ')
        for p in pesanan:
            print(f'{p["nama"]} {p["jumlah"]} x {p["harga"]} = {p["jumlah"]} * {p["harga"]} = {p["jumlah"]}')
        print(f'Total Harga: {total_harga}')
        print(f'Uang yang dibawa: {uang}')
        print(f'Kembalian: {uang - total_harga}')

class konsumen:
    def __init__(self, nama, uang):
        self.nama = nama
        self.uang = uang

    def pesan(self, kantin, pesanan):
        items = []
        for p in pesanan:
            item = {
                'nama' : p,
                'jumlah' : pesanan[p],
                'harga' : kantin.menu_makanan[p] if p in kantin.menu_makanan else kantin.menu_minuman[p]   
            }
            items.append(item)

        total_harga = 0
        for item in items:
            total_harga += item['jumlah'] * item['harga']

        if total_harga > self.uang:
            print('Maaf, uang Anda tidak cukup.')
        else:
            kantin.cetak_struk(self.nama, self.uang, items)

# contoh
kantin = kantin()

konsumen1 = konsumen('Haidar', 10000)
konsumen1.pesan(kantin, {'Kue Sus mini': 1, 'Susu': 1})

konsumen1 = konsumen('Jihad', 20000)
konsumen1.pesan(kantin, {'Makaroni': 2, 'Es Teh Manis': 1})