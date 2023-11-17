mahasiswa = {
    "nama"   : "Muhammad Haidar Jihad Izzuddin",
    "matkul" : "Dasar Pemograman",
    "nilai"  : 90
}

for i in mahasiswa.value():
    print(i)

for j in mahasiswa.keys():
    print(j)

for key, values in mahasiswa.items():
    print(key, ":", values)