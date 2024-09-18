print("jesli chcesz sprawdzic trojkat wybierz '1' jesli kwadratu lub prostokatu albo czworokata wybierz '2'")
wybor = input()

if wybor == '1':
    print("trojkat")
    a = float(input())
    b = float(input())
    c = float(input())
    
    if a + b > c and a + c > b and c + b > a:
        print("jest to trojkat")
        if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
            print("To jest trojkat prostkoatny")
        else:
            print("To nie jest trojkat prostkoatny")
            if a == b == c:
                print("to jest trojkat rownoboczny")
            else:
                print("to nie jest trojkat rownoboczny")
                if a == b or a == c or b == c:
                    print("to jest trojkat rownoramienny")
                else:
                    print("to nie jest trojkat rownoramienny")
                    if a != b or a != c or b != c:
                        print("to jest trojkat rozno boczny")
                    else:
                        print("to nie jest trojkat rozno boczny")
    else:
        print("Nie jest to trojkat")    
elif wybor == '2':
    print("kwadrat lub prostokat albo inny czworokat")
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    
    if a > 0 and b > 0 and c > 0 and d > 0:
        print("to jest kwadrat lub prostokat albo inny czworokat")
        if a == b == c == d:
            print("to jest kwadrat")
        else:
            print("to nie jest kwadrat")
            if a == b and c == d or a == c and b == d or a == d and b == c or b == c and a == d or b == d and a == c or c == d and a == d:
                print("to jest prostokat")
            else:
                print("to nie jest prostokat")
    else:
        print("to nie jest kwadrat lub prostokat albo inny czworokat")
else:
    print("zly wybor")
        