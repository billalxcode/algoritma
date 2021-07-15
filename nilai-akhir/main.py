"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
nama = input("Nama: ")
kehadiran = input("Jumlah kehadiran: ")
tugas = input("Jumlah nilai tugas: ")
kuis = input("Jumlah nilai kuis: ")
uts = input("Jumlah nilai UTS: ")
uas = input("Jumlah nilai UAS: ")

nilaiAkhir = (int(kehadiran) * 0.05) + (int(tugas) * 0.25) + (int(kuis) * 0.15) + (int(uts) * 0.25) + (int(uas) * 0.30)

print ("Nilai akhir: " + str(nilaiAkhir))