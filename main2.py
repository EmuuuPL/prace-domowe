import main1

print("wybierz numer figury od 1 do 9")

while True:
    print("1. Prostokąt")
    print("2. Kwadrat")
    print("3. Prostopadłościan")
    print("4. Sześcian")
    print("5. Kula")
    print("6. Walec")
    print("7. Stożek")
    print("8. Graniastosłup")
    print("9. Ostrosłup")

    wybor = int(input())
    if wybor == 1:
        print("wybrałeś prostokąt. co chcesz sprawdzić? 1. pole 2. obwód")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole prostokąta")
            a = float(input())
            b = float(input())
            print(f"Pole prostokąta: {main1.pole_prostokata(a, b)}")
        elif wybor2 == 2:
            print("wybrałeś obwód prostokąta")
            a = float(input())
            b = float(input())
            print(f"Obwód prostokąta: {main1.obwod_prostokata(a, b)}")
        break

    elif wybor == 2:
        print("wybrałeś kwadrat. co chcesz sprawdzić? 1. pole 2. obwód")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole kwadratu")
            a = float(input())
            print(f"Pole kwadratu: {main1.pole_kwadratu(a)}")
        elif wybor2 == 2:
            print("wybrałeś obwód kwadratu")
            a = float(input())
            print(f"Obwód kwadratu: {main1.obwod_kwadratu(a)}")
        break

    elif wybor == 3:
        print("wybrałeś prostopadłościan. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole prostopadłościanu")
            a = float(input())
            b = float(input())
            c = float(input())
            print(f"Pole prostopadłościanu: {main1.pole_prostopadloscianu(a, b, c)}")
        elif wybor2 == 2:
            print("wybrałeś objętość prostopadłościanu")
            a = float(input())
            b = float(input())
            c = float(input())
            print(f"Objętość prostopadłościanu: {main1.objetosc_prostopadloscianu(a, b, c)}")
        break

    elif wybor == 4:
        print("wybrałeś sześcian. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole sześcianu")
            a = float(input())
            print(f"Pole sześcianu: {main1.pole_szescianu(a)}")
        elif wybor2 == 2:
            print("wybrałeś objętość sześcianu")
            a = float(input())
            print(f"Objętość sześcianu: {main1.objetosc_szescianu(a)}")
        break

    elif wybor == 5:
        print("wybrałeś kulę. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole kuli")
            r = float(input())
            print(f"Pole kuli: {main1.pole_kuli(r)}")
        elif wybor2 == 2:
            print("wybrałeś objętość kuli")
            r = float(input())
            print(f"Objętość kuli: {main1.objetosc_kuli(r)}")
        break

    elif wybor == 6:
        print("wybrałeś walec. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole walca")
            r = float(input())
            H = float(input())
            print(f"Pole walca: {main1.pole_walca(r, H)}")
        elif wybor2 == 2:
            print("wybrałeś objętość walca")
            r = float(input())
            H = float(input())
            print(f"Objętość walca: {main1.objetosc_walca(r, H)}")
        break

    elif wybor == 7:
        print("wybrałeś stożek. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole stożka")
            r = float(input())
            l = float(input())
            print(f"Pole stożka: {main1.pole_stozka(r, l)}")
        elif wybor2 == 2:
            print("wybrałeś objętość stożka")
            r = float(input())
            H = float(input())
            print(f"Objętość stożka: {main1.objetosc_stozka(r, H)}")
        break

    elif wybor == 8:
        print("wybrałeś graniastosłup. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole graniastosłupa")
            Pp = float(input())
            H = float(input())
            print(f"Pole graniastosłupa: {main1.pole_graniastoslupa(Pp, H)}")
        elif wybor2 == 2:
            print("wybrałeś objętość graniastosłupa")
            Pp = float(input())
            H = float(input())
            print(f"Objętość graniastosłupa: {main1.objetosc_graniastoslupa(Pp, H)}")
        break

    elif wybor == 9:
        print("wybrałeś ostrosłup. co chcesz sprawdzić? 1. pole 2. objętość")
        wybor2 = int(input())
        if wybor2 == 1:
            print("wybrałeś pole ostrosłupa")
            Pp = float(input())
            Pb = float(input())
            print(f"Pole ostrosłupa: {main1.pole_ostroslupa(Pp, Pb)}")
        elif wybor2 == 2:
            print("wybrałeś objętość ostrosłupa")
            Pp = float(input())
            H = float(input())
            print(f"Objętość ostrosłupa: {main1.objetosc_ostroslupa(Pp, H)}")
        break

    else:
        print("Nieprawidłowy wybór")
        continue
