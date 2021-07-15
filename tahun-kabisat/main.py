"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
tahun = input("Tahun: ")

kabisat = False
bagi = [400, 100, 4]
for i in range(0, int(len(bagi))):
    x = bagi[i-1]
    if int(tahun) % x == 0:
        kabisat = True

print (f"Tahun {tahun} adalah " + ("Tahun kabisat" if kabisat else "Bukan tahun kabisat"))