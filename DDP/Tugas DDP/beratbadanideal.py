from tkinter import BitmapImage


berat =int(input("Berat Badan (kg) : "))
tinggi =int(input("Tinggi Badan (kg) : "))

tinggi = tinggi/100

bmi = berat / (tinggi**2)

print("Nlai BMI Anda : ",bmi)

if bmi < 18.5:
    print("Berat Badan anda Kurang ")
elif bmi > 18.5 and bmi < 24.9:
    print("Berat Badan anda Normal ")
elif bmi > 25 and bmi < 29.9:
    print("Anda Kelebihan Berat Badan ")
elif bmi > 30:
    print("Anda Obesitas")