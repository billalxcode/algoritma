"""
Copyright (c) 2021 Billal Fauzan
Created: 15 Juli 2021
"""
import random
import time

start = time.time()
payung = 0
hujan = random.randint(0, 1)
if hujan == 1:
    print ("Sedang mencari payung")
    while True:
        barang = ["Jas Hujan", "Payung", "Sarung Tas",
            "Sarung Sepatu", "Sendal Jepit", "Handuk", "Minyak Angin"]
        cariBarang = barang[random.randint(0, int(len(barang))-1)]
        time.sleep(1)
        if cariBarang.lower() == "payung":
            print ("Payung ketemu")
            end = time.time()
            waktu = float(end - start)
            print ("Waktu: " + str(waktu))
            break
        else:
            print ("Mencari...") 
else:
    print ("Tidak hujan")