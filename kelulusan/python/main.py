"""
Copyright (c) 2021 Billal Fauzan
Created: 15 Juli 2021
"""

def checkIsGraduated():
    nama = input("Nama: ")
    nilai = input("Nilai: ")

    try:
        if int(nilai) > 70:
            keterangan = "Lulus"
        else:
            keterangan = "Tidak lulus"

        print ("Nama: " + nama)
        print ("Nilai: " + str(nilai))
        print ("Keterangan: " + keterangan)
    except ValueError:
        raise ValueError(f'Bilangan {nilai} bukan integer')
if __name__ == '__main__':
    checkIsGraduated()