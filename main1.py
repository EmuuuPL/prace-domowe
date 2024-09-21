import math

def pole_szescianu(a):
    return 6 * a ** 2

def objetosc_szescianu(a):
    return a ** 3

def pole_prostopadloscianu(a, b, c):
    return 2 * (a*b + b*c + a*c)

def objetosc_prostopadloscianu(a, b, c):
    return a * b * c

def pole_kwadratu(a):
    return a ** 2

def obwod_kwadratu(a):
    return 4 * a

def pole_prostokata(a, b):
    return a * b

def obwod_prostokata(a, b):
    return 2 * (a + b)

def pole_trojkata(a, h):
    return 0.5 * a * h

def obwod_trojkata(a, b, c):
    return a + b + c

def pole_trapezu(a, b, h):
    return 0.5 * (a + b) * h

def obwod_trapezu(a, b, c, d):
    return a + b + c + d

def pole_kola(r):
    return math.pi * r ** 2

def obwod_kola(r):
    return 2 * math.pi * r

def pole_walca(r, h):
    return 2 * math.pi * r * (r + h)

def objetosc_walca(r, h):
    return math.pi * r ** 2 * h

def pole_stozka(r, s):
    return math.pi * r * (r + s)

def objetosc_stozka(r, h):
    return (1/3) * math.pi * r ** 2 * h

def pole_kuli(r):
    return 4 * math.pi * r ** 2

def objetosc_kuli(r):
    return (4/3) * math.pi * r ** 3

def main():
    while True:
        print("\nWybierz figurę:")
        print("1. Sześcian")
        print("2. Prostopadłościan")
        print("3. Kwadrat")
        print("4. Prostokąt")
        print("5. Trójkąt")
        print("6. Trapez")
        print("7. Koło")
        print("8. Walec")
        print("9. Stożek")
        print("10. Kula")
        print("0. Wyjście")
        
        wybor = input("Twój wybór: ")
        
        if wybor == '0':
            break
        
        if wybor == '1':
            a = float(input("Podaj długość boku sześcianu: "))
            print(f"Pole powierzchni: {pole_szescianu(a)}")
            print(f"Objętość: {objetosc_szescianu(a)}")
        elif wybor == '2':
            a = float(input("Podaj długość: "))
            b = float(input("Podaj szerokość: "))
            c = float(input("Podaj wysokość: "))
            print(f"Pole powierzchni: {pole_prostopadloscianu(a, b, c)}")
            print(f"Objętość: {objetosc_prostopadloscianu(a, b, c)}")
        elif wybor == '3':
            a = float(input("Podaj długość boku kwadratu: "))
            print(f"Pole: {pole_kwadratu(a)}")
            print(f"Obwód: {obwod_kwadratu(a)}")
        elif wybor == '4':
            a = float(input("Podaj długość: "))
            b = float(input("Podaj szerokość: "))
            print(f"Pole: {pole_prostokata(a, b)}")
            print(f"Obwód: {obwod_prostokata(a, b)}")
        elif wybor == '5':
            a = float(input("Podaj podstawę trójkąta: "))
            h = float(input("Podaj wysokość trójkąta: "))
            print(f"Pole: {pole_trojkata(a, h)}")
            b = float(input("Podaj drugi bok trójkąta: "))
            c = float(input("Podaj trzeci bok trójkąta: "))
            print(f"Obwód: {obwod_trojkata(a, b, c)}")
        elif wybor == '6':
            a = float(input("Podaj pierwszą podstawę trapezu: "))
            b = float(input("Podaj drugą podstawę trapezu: "))
            h = float(input("Podaj wysokość trapezu: "))
            print(f"Pole: {pole_trapezu(a, b, h)}")
            c = float(input("Podaj trzeci bok trapezu: "))
            d = float(input("Podaj czwarty bok trapezu: "))
            print(f"Obwód: {obwod_trapezu(a, b, c, d)}")
        elif wybor == '7':
            r = float(input("Podaj promień koła: "))
            print(f"Pole: {pole_kola(r)}")
            print(f"Obwód: {obwod_kola(r)}")
        elif wybor == '8':
            r = float(input("Podaj promień podstawy walca: "))
            h = float(input("Podaj wysokość walca: "))
            print(f"Pole powierzchni: {pole_walca(r, h)}")
            print(f"Objętość: {objetosc_walca(r, h)}")
        elif wybor == '9':
            r = float(input("Podaj promień podstawy stożka: "))
            h = float(input("Podaj wysokość stożka: "))
            s = float(input("Podaj długość tworzącej stożka: "))
            print(f"Pole powierzchni: {pole_stozka(r, s)}")
            print(f"Objętość: {objetosc_stozka(r, h)}")
        elif wybor == '10':
            r = float(input("Podaj promień kuli: "))
            print(f"Pole powierzchni: {pole_kuli(r)}")
            print(f"Objętość: {objetosc_kuli(r)}")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()