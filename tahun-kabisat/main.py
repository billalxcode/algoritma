"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
Updated: 04 Oktober 2021
"""
tahun = input("Tahun: ")

kabisat = False
bagi = [400, 100, 4]
for x in bagi:
    if int(tahun) % x == 0:
        kabisat = True

print (f"Tahun {tahun} adalah " + ("Tahun kabisat" if kabisat else "Bukan tahun kabisat"))