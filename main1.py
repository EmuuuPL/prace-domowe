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

def pole_rownolegloboku(a, h):
    return a * h

def obwod_rownolegloboku(a, b):
    return 2 * (a + b)

def pole_graniastoslupa(Pp, Pb):
    return 2 * Pp + Pb

def objetosc_graniastoslupa(Pp, H):
    return Pp * H

def pole_ostroslupa(Pp, Pb):
    return Pp + Pb

def objetosc_ostroslupa(Pp, H):
    return (1/3) * Pp * H

def pole_walca(r, H):
    return 2 * math.pi * r * (r + H)

def objetosc_walca(r, H):
    return math.pi * r ** 2 * H

def pole_stozka(r, l):
    return math.pi * r * (r + l)

def objetosc_stozka(r, H):
    return (1/3) * math.pi * r ** 2 * H

def pole_kuli(r):
    return 4 * math.pi * r ** 2

def objetosc_kuli(r):
    return (4/3) * math.pi * r ** 3

def pole_trapezu(a, b, h):
    return (a + b) * h / 2

def obwod_trapezu(a, b, c, d):
    return a + b + c + d

def pole_trojkata(a, h):
    return a * h / 2

def obwod_trojkata(a, b, c):
    return a + b + c

def pole_trojkata_rownobocznego(a):
    return (a ** 2 * math.sqrt(3)) / 4

def obwod_trojkata_rownobocznego(a):
    return 3 * a

def pole_kola(r):
    return math.pi * r ** 2

def obwod_kola(r):
    return 2 * math.pi * r

def pole_rombu(a, h):
    return a * h

def obwod_rombu(a):
    return 4 * a

def wysokosc_trojkata_rownobocznego(a):
    return (a * math.sqrt(3)) / 2

def przekatna_kwadratu(a):
    return a * math.sqrt(2)

def twierdzenie_pitagorasa(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    while True:
        print("\nWybierz figurę lub działanie:")
        print("1. Sześcian")
        print("2. Prostopadłościan")
        print("3. Kwadrat")
        print("4. Prostokąt")
        print("5. Równoległobok")
        print("6. Graniastosłup")
        print("7. Ostrosłup")
        print("8. Walec")
        print("9. Stożek")
        print("10. Kula")
        print("11. Trapez")
        print("12. Trójkąt")
        print("13. Trójkąt równoboczny")
        print("14. Koło")
        print("15. Romb")
        print("16. Twierdzenie Pitagorasa")
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
            print(f"Przekątna: {przekatna_kwadratu(a)}")
        elif wybor == '4':
            a = float(input("Podaj długość: "))
            b = float(input("Podaj szerokość: "))
            print(f"Pole: {pole_prostokata(a, b)}")
            print(f"Obwód: {obwod_prostokata(a, b)}")
        elif wybor == '5':
            a = float(input("Podaj długość podstawy: "))
            h = float(input("Podaj wysokość: "))
            b = float(input("Podaj długość boku: "))
            print(f"Pole: {pole_rownolegloboku(a, h)}")
            print(f"Obwód: {obwod_rownolegloboku(a, b)}")
        elif wybor == '6':
            Pp = float(input("Podaj pole podstawy: "))
            Pb = float(input("Podaj pole boczne: "))
            H = float(input("Podaj wysokość: "))
            print(f"Pole powierzchni: {pole_graniastoslupa(Pp, Pb)}")
            print(f"Objętość: {objetosc_graniastoslupa(Pp, H)}")
        elif wybor == '7':
            Pp = float(input("Podaj pole podstawy: "))
            Pb = float(input("Podaj pole boczne: "))
            H = float(input("Podaj wysokość: "))
            print(f"Pole powierzchni: {pole_ostroslupa(Pp, Pb)}")
            print(f"Objętość: {objetosc_ostroslupa(Pp, H)}")
        elif wybor == '8':
            r = float(input("Podaj promień podstawy walca: "))
            H = float(input("Podaj wysokość walca: "))
            print(f"Pole powierzchni: {pole_walca(r, H)}")
            print(f"Objętość: {objetosc_walca(r, H)}")
        elif wybor == '9':
            r = float(input("Podaj promień podstawy stożka: "))
            H = float(input("Podaj wysokość stożka: "))
            l = float(input("Podaj długość tworzącej stożka: "))
            print(f"Pole powierzchni: {pole_stozka(r, l)}")
            print(f"Objętość: {objetosc_stozka(r, H)}")
        elif wybor == '10':
            r = float(input("Podaj promień kuli: "))
            print(f"Pole powierzchni: {pole_kuli(r)}")
            print(f"Objętość: {objetosc_kuli(r)}")
        elif wybor == '11':
            a = float(input("Podaj długość pierwszej podstawy: "))
            b = float(input("Podaj długość drugiej podstawy: "))
            h = float(input("Podaj wysokość: "))
            c = float(input("Podaj długość pierwszego boku: "))
            d = float(input("Podaj długość drugiego boku: "))
            print(f"Pole: {pole_trapezu(a, b, h)}")
            print(f"Obwód: {obwod_trapezu(a, b, c, d)}")
        elif wybor == '12':
            a = float(input("Podaj długość podstawy: "))
            h = float(input("Podaj wysokość: "))
            b = float(input("Podaj długość drugiego boku: "))
            c = float(input("Podaj długość trzeciego boku: "))
            print(f"Pole: {pole_trojkata(a, h)}")
            print(f"Obwód: {obwod_trojkata(a, b, c)}")
        elif wybor == '13':
            a = float(input("Podaj długość boku trójkąta równobocznego: "))
            print(f"Pole: {pole_trojkata_rownobocznego(a)}")
            print(f"Obwód: {obwod_trojkata_rownobocznego(a)}")
            print(f"Wysokość: {wysokosc_trojkata_rownobocznego(a)}")
        elif wybor == '14':
            r = float(input("Podaj promień koła: "))
            print(f"Pole: {pole_kola(r)}")
            print(f"Obwód: {obwod_kola(r)}")
        elif wybor == '15':
            a = float(input("Podaj długość boku rombu: "))
            h = float(input("Podaj wysokość rombu: "))
            print(f"Pole: {pole_rombu(a, h)}")
            print(f"Obwód: {obwod_rombu(a)}")
        elif wybor == '16':
            a = float(input("Podaj długość pierwszego przyprostokątnej: "))
            b = float(input("Podaj długość drugiej przyprostokątnej: "))
            c = twierdzenie_pitagorasa(a, b)
            print(f"Długość przeciwprostokątnej: {c}")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()