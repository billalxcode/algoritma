"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
import datetime

tahunSekarang = datetime.datetime.now().year
tahunLahir = input("Tahun lahir: " )
umur = tahunSekarang - int(tahunLahir)
print ("Umur: " + str(umur))