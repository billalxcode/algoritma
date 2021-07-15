"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
import random

def tampilMenu():
    menu = ["Nasi goreng", "Mie Ayam", "Bakso", "Nasi Padang", "Nasi Kuning"]
    for i in range(0, int(len(menu))):
        i += 1
        print (f"{str(i)}. {menu[i-1]}")
    pilihMakanan = input("Pilih: ")
    makanan = menu[int(pilihMakanan) - 1]
    return makanan

while True:
    makanan = tampilMenu()
    jadiPesan = input("Pesan? (Y/n): ")
    if jadiPesan.lower() == "y":
        stok = random.randint(0, 30)
        if stok >= 1:
            bayar = input("Bayar: ")
            if int(bayar) >= 10001:
                print ("selesai")
                break
            else:
                print ("Uang tidak cukup")
                break
        else:
            print ("Stok habis")