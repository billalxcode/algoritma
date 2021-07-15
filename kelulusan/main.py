"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""

nama = input("Nama: ")
nilai = input("Nilai: ")

if int(nilai) > 70:
    ketengan = "Lulus"
else:
    ketengan = "Tidak lulus"

print ("Nama: " + nama)
print ("Nilai: " + str(nilai))
print ("Keterangan: " + ketengan)