"""
Copyright (c) 2021 Billal Fauzan

Created: 15 Juli 2021
"""
def temperature_conversion():
    suhu = input("Suhu Celcius: ")
    try:
        F = (9/5) * int(suhu) + 32
        R = (4/5) * int(suhu)
        print ("Farenheit: " + str(F))
        print ("Reamur: " + str(R))
        return(F, R)
    except ValueError:
        raise ValueError(f'Bilangan {suhu} bukan integer')
    except TypeError:
        raise TypeError((f'Bilangan {suhu} bukan integer'))

if __name__ == '__main__':
    temperature_conversion()