a = 6
for atas in range (0, a):
    for bawah in range (0, atas):
        print("*", end="")
    print("")

for atas in range (0, a):
    for bawah in range (0, a):
        print("*", end="")
    a-=1
    print("")