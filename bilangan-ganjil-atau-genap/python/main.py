"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
def isEvenOrOdd():
    bilangan = input("Masukan bilangan: ")
    try:
        sisa = int(bilangan) % 2
        if sisa == 0:
            print ("Genap")
            return sisa
        print ("Ganjil")
        return sisa
    except ValueError:
        raise ValueError(f'Bilangan {bilangan} bukan integer')
    except TypeError:
        raise TypeError(f'Type {bilangan} bukan integer')
    except Exception:
        raise

if __name__ == '__main__':
    isEvenOrOdd()