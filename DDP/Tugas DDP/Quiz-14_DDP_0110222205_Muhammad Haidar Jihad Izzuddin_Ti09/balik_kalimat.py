def balik_kalimat(kata):
    kalimat_balik = ""

    kalimat = kata.split()

    for i in range(len(kalimat)):

        kalimat_balik += kalimat[-i-1] + " "
    return kalimat_balik

print(balik_kalimat("saya mahasiswa Nurul Fikri"))
print(balik_kalimat("saya prodi Teknik Informatika"))
print(balik_kalimat("Pemograman Dasar menyenangkan"))
