angka1 = int(input('Masukan angka 1 : '))
angka2 = int(input('Masukan angka 2 : '))

operator = input('Masukan operasi yagn diinginkan : ')

if operator == 'Tambah' :
    hasil = angka1+angka2
elif operator == 'Kurang' :
    hasil = angka1-angka2
elif operator == 'Bagi' :
    hasil = angka1/angka2
elif operator == 'Kali' :
    hasil = angka1*angka2
elif operator == 'Pangkat' :
    hasil = angka1**angka2
else :
    hasil = 'Salah input operasi'

print("Angka pertama : ",angka1)
print("Angka kedua : ",angka2)
print('Pilihan Operator = ', operator)
print('Hasil operator ',angka1, "x", angka2 ,"=", hasil)