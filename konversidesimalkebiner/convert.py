#!/usr/bin/python
# Menghitung Bilangan Desimal Ke Biner


while True:
    bil =  input("Bilangan: ")
    out = ""
    print("")
    while True:
        bil = str(int(bil)/2)

        if ".0" in bil:
            print(f"Hasil: {bil.split('.')[0]} sisa 0")
            out += "0"
        else:
            print(f"Hasil: {bil.split('.')[0]} sisa 1")
            out += "1"

        if bil.split(".")[0] == "0":
            break

        bil = bil.split(".")[0]

    print(f"\nOUTPUT: {out[::-1]}\n")
