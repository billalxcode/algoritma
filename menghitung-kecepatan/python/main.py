"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
def calculateSpeed():
    try:
        jarak = input("Jarak (km): ")
        waktu = input("waktu (jam): ")
        kecepatan = int(jarak) / int(waktu)
        print (f"Hasil: {kecepatan}/jam")
    except ValueError:
        raise ValueError(f'Bilangan {jarak}/{waktu} bukan integer')

if __name__ == "__main__":
    calculateSpeed()