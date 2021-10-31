"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""

def calculateAreaRectangle():
    try:
        wide = input("Wide: ")
        length = input("Length: ")
        area = int(length) * int(wide)
        print(f"Hasil: {area}")
    except ValueError:
        raise ValueError(f'Bilangan {wide}*{length} bukan integer')

if __name__ == '__main__':
    calculateAreaRectangle()