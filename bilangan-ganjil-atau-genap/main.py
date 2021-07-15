"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
bilangan = input("Masukan bilangan: ")
sisa = int(bilangan) % 2
if sisa == 0:
    print ("Genap")
else:
    print ("Ganjil")