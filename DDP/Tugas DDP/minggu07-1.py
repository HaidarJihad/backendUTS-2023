kenda = input("Nama kendaraan yang akan anda gunakan (Mobil, motor) : ")
bensi = input("Nama bensin yang akan Anda Gunakan : ")
kota = input("NAma kota tujuan : ")

if bensi == 'pertalite':
    harga = 10000
    jarak = 12
elif bensi == 'pertamax':
    harga = 14000
    jarak = 13
elif bensi == 'pertamax Turbo':
    harga = 17000
    jarak = 13.5

if kota == 'jakarta' :
    jauh = 20
if kota == 'Bekasi' :
    jauh = 35.7
if kota == 'Depok' :
    jauh = 5
if kota == 'Tangerng' :
    jauh = 99
if kota == 'Bogor' :
    jauh = 120.6

pem = jauh/jarak
total = pem*harga

print (kenda)
print(bensi)
print(kota)
print (pem, 'liter')
print('Rp ',total)