print("\nKomversi Celcius\n")

celcius = float(input("Masukkan nilai Celcius : "))
fahreinheit = (9/5) * celcius + 32
reamur = (4/5) * celcius

print("Nilai Celcius : ",celcius, "C")
print("Nilai fahreinheit : ",fahreinheit, "F")
print("Nilai reamur : ",reamur, "R")


print("\nKomversi Fahreinheit\n")

fahreinheit = float(input("Masukkan nilai Fahreinheit : "))
celcius = (5/9) * (fahreinheit - 32)
reamur = (4/9) * (fahreinheit - 32)

print("Nilai fahreinheit : ", fahreinheit, "F")
print("Nilai celcius : ", celcius, "C")
print("Nilai reamur : ", reamur, "R")

print("\nKomversi Reamur\n")

reamur = float(input("Masukkan nilai Reamur : "))
celcius = (5/4) * reamur
fahreinheit = (9/4) * reamur + 32

print("Nilai reamur : ", reamur, "R")
print("Nilai celcius : ", celcius, "C")
print("Nilai fahreinheit : ", fahreinheit, "F")