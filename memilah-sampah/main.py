"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
import random
import time

sampah = {"Tisu": 1, "Sisa Sayuran": 1, "Sisa Buahan": 1, "Kertas": 1, 
    "Daun bungkus kaca": 1, "Daun kering": 1, "Botol kaca": 0, "Botol plastik": 0,
    "Styrofoam": 0, "Mainan Plastik": 0, "Plastik makanan": 0, "Kantong plastik": 0}

start = time.time()
pupuk = 0
dimanfaatkan = 0
daurUlang = 0
pembuanganAkhir = 0

carisampah = random.randint(0, int(len(list(sampah)))) - 1
print ("Sampah: " + list(sampah)[carisampah])
isSampahOrganik = list(sampah)[carisampah]
if isSampahOrganik == 0:
    gunakanKembali = random.randint(0, 1)
    if gunakanKembali == 1:
        dimanfaatkan = 1
    else:
        daurUlang = random.randint(0, 1)
        if daurUlang == 1:
            daurUlang = 1
        else:
            pembuanganAkhir = 1
else:
    pupuk = 1

print ("Dijadikan pupuk: " + ("iya" if pupuk == 1 else "tidak"))
print ("Dimanfaatkan kembali: " + ("iya" if dimanfaatkan == 1 else "tidak"))
print ("Didaur ulang: " + ("iya" if daurUlang == 1 else "tidak"))
print ("Pembuangan akhir: " + ("iya" if pembuanganAkhir == 1 else "tidak"))