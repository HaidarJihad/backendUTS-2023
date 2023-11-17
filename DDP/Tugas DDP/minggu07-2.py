nama= input("NAma anda: ")
nohp= int (input("Nomor hp anda: "))
pesan= input("PEsan makanan/minuman: ")

if pesan == "Makanan":
    print("MEnu makanan: nasi goreng (RP.15000), mie goreng(RP.12000), ayam geprek(Rp.18000)")
    menu= input("Pesanan anda: ")

    if menu == "Nasi goreng":
        harga= 15000
    elif menu == "MIe goreng":
        harga= 12000
    elif menu == "Ayam geprek":
        harga= 18000
    else:
        print("Menu tidak tersedia")

elif pesan == "Minuman":
    print("MEnu minuman: aneka jus(RP.15000), soft drink(RP.10000), sweet ice tea(RP.5000)")
    menu= input("Pesanan anda: ")

    if menu == "ANeka jus":
        harga= 15000
    elif menu == "Soft drink":
        harga= 10000
    elif menu == "Sweet ice tea":
        harga= 5000
    else:
        print("Menu tidak tersedia")
else:
    print("Ulangi")

jumlah = int(input("Jumlah yang diinginkan: "))

total= jumlah*harga

#output
print("NAma anda:", nama)
print("Nomor hp: ", nohp)
print("MEnu anda: ", menu)
print("Jumlah: ", jumlah)
print("Harga yang harus dibayar: ", total)