import pygame
import sys
import random
import time

pygame.init()

szerokość = 800
wysokość = 600

okno = pygame.display.set_mode((szerokość, wysokość))
pygame.display.set_caption("Gra Pong")

JASNY_NIEBIESKI = (173, 216, 230)  # Nowy kolor tła
CZARNY = (0, 0, 0)
NIEBIESKI = (0, 0, 255)
CZERWONY = (255, 0, 0)
SZARY = (200, 200, 200)
POMARAŃCZOWY = (255, 165, 0)  # Nowy kolor piłki
BIALY = (255, 255, 255)  # Dodany kolor biały

# Platformy
platforma_szerokość = 15
platforma_wysokość = 90
platforma_lewa = pygame.Rect(50, wysokość//2 - platforma_wysokość//2, platforma_szerokość, platforma_wysokość)
platforma_prawa = pygame.Rect(szerokość - 50 - platforma_szerokość, wysokość//2 - platforma_wysokość//2, platforma_szerokość, platforma_wysokość)

prędkość_platform = 5

# Piłka
piłka_rozmiar = 15
piłka = pygame.Rect(szerokość//2 - piłka_rozmiar//2, wysokość//2 - piłka_rozmiar//2, piłka_rozmiar, piłka_rozmiar)
początkowa_prędkość = 4
piłka_prędkość = początkowa_prędkość
piłka_dx = piłka_prędkość * random.choice((1, -1))
piłka_dy = piłka_prędkość * random.choice((1, -1))
przyspieszenie = 0.1

# Bramki
bramka_szerokość = 10
bramka_wysokość = 200
bramka_lewa = pygame.Rect(0, wysokość//2 - bramka_wysokość//2, bramka_szerokość, bramka_wysokość)
bramka_prawa = pygame.Rect(szerokość - bramka_szerokość, wysokość//2 - bramka_wysokość//2, bramka_szerokość, bramka_wysokość)

# Licznik punktów
punkty_lewy = 0
punkty_prawy = 0
czcionka = pygame.font.Font(None, 36)

# Timer
czas_początkowy = time.time()
czas_gry = 0

zegar = pygame.time.Clock()

# Wybór trybu gry i strony gracza
tryb_dwoch_graczy = None
gracz_po_lewej = None

MAX_PUNKTY = 10
MAX_CZAS = 300  # 300 sekund = 5 minut

# Dodajemy zmienną poziomu trudności
poziom_trudności = None

# Ustawienia gry (domyślne wartości)
MAX_PUNKTY = 10
MAX_CZAS = 300  # 300 sekund = 5 minut
początkowa_prędkość = 4
przyspieszenie = 0.1
czy_przyspieszać = True

czcionka = pygame.font.Font(None, 36)
czcionka_mała = pygame.font.Font(None, 24)

def rysuj_tekst(tekst, x, y, kolor=CZARNY):
    powierzchnia = czcionka.render(tekst, True, kolor)
    okno.blit(powierzchnia, (x, y))

def rysuj_mały_tekst(tekst, x, y, kolor=CZARNY):
    powierzchnia = czcionka_mała.render(tekst, True, kolor)
    okno.blit(powierzchnia, (x, y))

def pobierz_wartość(prompt, typ=int):
    wartość = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        return typ(wartość)
                    except ValueError:
                        rysuj_tekst("Nieprawidłowa wartość, spróbuj ponownie.", 100, 300)
                elif event.key == pygame.K_BACKSPACE:
                    wartość = wartość[:-1]
                elif event.unicode.isdigit() or (event.unicode == '.' and '.' not in wartość):
                    wartość += event.unicode
        
        okno.fill(BIALY)
        rysuj_tekst(prompt, 100, 200)
        rysuj_tekst(wartość, 100, 250)
        pygame.display.flip()

def panel_sterowania():
    global MAX_PUNKTY, MAX_CZAS, początkowa_prędkość, przyspieszenie, czy_przyspieszać
    
    wybrana_opcja = 0
    opcje = [
        ("Punkty do wygranej:", MAX_PUNKTY, int),
        ("Maksymalny czas gry (s):", MAX_CZAS, int),
        ("Początkowa prędkość piłki:", początkowa_prędkość, float),
        ("Przyspieszanie piłki:", czy_przyspieszać, bool),
        ("Wartość przyspieszenia:", przyspieszenie, float)
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Zaktualizuj globalne zmienne po zakończeniu panelu
                    MAX_PUNKTY = opcje[0][1]
                    MAX_CZAS = opcje[1][1]
                    początkowa_prędkość = opcje[2][1]
                    czy_przyspieszać = opcje[3][1]
                    przyspieszenie = opcje[4][1]
                    czas_początkowy = time.time()
                    return
                elif event.key == pygame.K_UP:
                    wybrana_opcja = (wybrana_opcja - 1) % len(opcje)
                elif event.key == pygame.K_DOWN:
                    wybrana_opcja = (wybrana_opcja + 1) % len(opcje)
                elif event.key == pygame.K_SPACE:
                    tekst, wartość, typ = opcje[wybrana_opcja]
                    if typ == bool:
                        opcje[wybrana_opcja] = (tekst, not wartość, typ)
                    else:
                        nowa_wartość = pobierz_wartość(f"Podaj nową wartość dla {tekst}", typ)
                        if nowa_wartość is not None:
                            opcje[wybrana_opcja] = (tekst, nowa_wartość, typ)

        okno.fill(BIALY)
        rysuj_tekst("Panel Sterowania", 250, 50)
        for i, (tekst, wartość, _) in enumerate(opcje):
            kolor = CZERWONY if i == wybrana_opcja else CZARNY
            rysuj_mały_tekst(f"{i+1}. {tekst} {wartość}", 100, 150 + i*50, kolor)
        
        rysuj_mały_tekst("Użyj strzałek do nawigacji, SPACJA aby zmienić wartość, ENTER aby rozpocząć grę", 50, 450)
        pygame.display.flip()

def zwiększ_prędkość():
    global piłka_dx, piłka_dy, piłka_prędkość
    if czy_przyspieszać:
        piłka_prędkość += przyspieszenie
        piłka_dx = piłka_prędkość * (1 if piłka_dx > 0 else -1)
        piłka_dy = piłka_prędkość * (1 if piłka_dy > 0 else -1)

def resetuj_piłkę():
    global piłka_dx, piłka_dy, piłka_prędkość
    piłka.center = (szerokość//2, wysokość//2)
    piłka_prędkość = początkowa_prędkość
    piłka_dx = piłka_prędkość * random.choice((1, -1))
    piłka_dy = piłka_prędkość * random.choice((1, -1))

def przewiduj_pozycję_piłki(piłka, dx, dy, poziom):
    przewidywana_x = piłka.x
    przewidywana_y = piłka.y
    max_odbić = 1 if poziom == "łatwy" else (2 if poziom == "średni" else 3)
    
    for _ in range(max_odbić):
        przewidywana_x += dx
        przewidywana_y += dy
        
        if przewidywana_y <= 0 or przewidywana_y >= wysokość:
            dy = -dy
        
        if przewidywana_x <= 0 or przewidywana_x >= szerokość:
            break
    
    return przewidywana_y

def ruch_si(platforma, piłka, poziom):
    if poziom == "łatwy":
        prędkość_si = prędkość_platform * 0.6
        błąd = random.randint(-50, 50)
    elif poziom == "średni":
        prędkość_si = prędkość_platform * 0.8
        błąd = random.randint(-30, 30)
    else:  # trudny
        prędkość_si = prędkość_platform * 1.0
        błąd = random.randint(-10, 10)

    przewidywana_y = przewiduj_pozycję_piłki(piłka, piłka_dx, piłka_dy, poziom)
    cel = przewidywana_y + błąd

    if platforma.centery < cel and platforma.bottom < wysokość:
        platforma.y += prędkość_si
    elif platforma.centery > cel and platforma.top > 0:
        platforma.y -= prędkość_si

def odbij_od_ściany():
    global piłka_dy
    piłka_dy = -piłka_dy
    
    # Upewnij się, że piłka nie jest wewnątrz ściany
    if piłka.top <= 0:
        piłka.top = 0
    elif piłka.bottom >= wysokość:
        piłka.bottom = wysokość
    
    zwiększ_prędkość()

def odbij_od_platformy(platforma):
    global piłka_dx, piłka_dy, piłka_prędkość
    
    # Oblicz względną pozycję uderzenia piłki na platformie
    względna_pozycja_y = (piłka.centery - platforma.top) / platforma.height
    
    # Zmień kąt odbicia w zależności od miejsca uderzenia
    piłka_dy = piłka_prędkość * (2 * względna_pozycja_y - 1)
    
    # Upewnij się, że piłka nie jest wewnątrz platformy
    if piłka_dx > 0:
        piłka.right = platforma.left
    else:
        piłka.left = platforma.right
    
    piłka_dx = -piłka_dx
    
    zwiększ_prędkość()

def odbij_od_bocznej_ściany():
    global piłka_dx
    piłka_dx = -piłka_dx
    
    # Upewnij się, że piłka nie jest wewnątrz ściany
    if piłka.left <= 0:
        piłka.left = 0
    elif piłka.right >= szerokość:
        piłka.right = szerokość
    
    zwiększ_prędkość()

def rysuj_tło():
    okno.fill(JASNY_NIEBIESKI)
    # Narysuj linię środkową
    pygame.draw.line(okno, SZARY, (szerokość // 2, 0), (szerokość // 2, wysokość), 2)

def wyświetl_zwycięzcę(zwycięzca):
    tekst_zwycięzca = czcionka.render(f"{zwycięzca} wygrywa!", True, CZARNY)
    rect_zwycięzca = tekst_zwycięzca.get_rect(center=(szerokość//2, wysokość//2))
    okno.blit(tekst_zwycięzca, rect_zwycięzca)
    pygame.display.flip()
    time.sleep(3)  # Wyświetl informację przez 3 sekundy

# Wybór trybu gry
czcionka_menu = pygame.font.Font(None, 48)
tekst_wyboru_trybu = czcionka_menu.render("Wybierz tryb: 1 - Jeden gracz, 2 - Dwóch graczy", True, CZARNY)
rect_wyboru_trybu = tekst_wyboru_trybu.get_rect(center=(szerokość//2, wysokość//2))

wybrano_tryb = False
while not wybrano_tryb:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tryb_dwoch_graczy = False
                wybrano_tryb = True
            elif event.key == pygame.K_2:
                tryb_dwoch_graczy = True
                wybrano_tryb = True

    okno.fill(BIALY)
    okno.blit(tekst_wyboru_trybu, rect_wyboru_trybu)
    pygame.display.flip()

# Wybór strony gracza (tylko dla trybu jednego gracza)
if not tryb_dwoch_graczy:
    tekst_wyboru = czcionka_menu.render("Wybierz stronę: L - Lewa, P - Prawa", True, CZARNY)
    rect_wyboru = tekst_wyboru.get_rect(center=(szerokość//2, wysokość//2))

    wybrano = False
    while not wybrano:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    gracz_po_lewej = True
                    wybrano = True
                elif event.key == pygame.K_p:
                    gracz_po_lewej = False
                    wybrano = True

        okno.fill(BIALY)
        okno.blit(tekst_wyboru, rect_wyboru)
        pygame.display.flip()

# Wybór poziomu trudności
if not tryb_dwoch_graczy:
    czcionka_menu = pygame.font.Font(None, 36)

    def wybierz_poziom_trudności():
        global poziom_trudności
        
        while poziom_trudności is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        poziom_trudności = "łatwy"
                    elif event.key == pygame.K_2:
                        poziom_trudności = "średni"
                    elif event.key == pygame.K_3:
                        poziom_trudności = "trudny"

            okno.fill(JASNY_NIEBIESKI)
            tekst1 = czcionka_menu.render("Wybierz poziom trudności:", True, CZARNY)
            tekst2 = czcionka_menu.render("1 - Łatwy, 2 - Średni, 3 - Trudny", True, CZARNY)
            okno.blit(tekst1, (szerokość//2 - tekst1.get_width()//2, wysokość//2 - 50))
            okno.blit(tekst2, (szerokość//2 - tekst2.get_width()//2, wysokość//2 + 50))
            pygame.display.flip()

    # Wywołujemy funkcję wyboru poziomu trudności przed główną pętlą gry
    wybierz_poziom_trudności()

# Wywołaj panel sterowania przed rozpoczęciem gry
panel_sterowania()
czas_początkowy = time.time()  # Rozpocznij timer po zakończeniu panelu sterowania
# Zresetuj piłkę z nową początkową prędkością
resetuj_piłkę()

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aktualizacja timera
    czas_gry = int(time.time() - czas_początkowy)
    
    # Sprawdzenie czy czas gry nie przekroczył limitu
    if czas_gry >= MAX_CZAS:
        if punkty_lewy > punkty_prawy:
            wyświetl_zwycięzcę("Lewy gracz")
        elif punkty_prawy > punkty_lewy:
            wyświetl_zwycięzcę("Prawy gracz kliknij enter aby zacząć nową grę")
        else:
            wyświetl_zwycięzcę("Remis kliknij enter aby zacząć nową grę")
        punkty_lewy = 0
        punkty_prawy = 0
        czas_początkowy = time.time()
        resetuj_piłkę()

    # Obsługa ruchu platform
    klawisze = pygame.key.get_pressed()
    if tryb_dwoch_graczy:
        if klawisze[pygame.K_w] and platforma_lewa.top > 0:
            platforma_lewa.y -= prędkość_platform
        if klawisze[pygame.K_s] and platforma_lewa.bottom < wysokość:
            platforma_lewa.y += prędkość_platform
        if klawisze[pygame.K_UP] and platforma_prawa.top > 0:
            platforma_prawa.y -= prędkość_platform
        if klawisze[pygame.K_DOWN] and platforma_prawa.bottom < wysokość:
            platforma_prawa.y += prędkość_platform
    else:
        if gracz_po_lewej:
            if klawisze[pygame.K_w] and platforma_lewa.top > 0:
                platforma_lewa.y -= prędkość_platform
            if klawisze[pygame.K_s] and platforma_lewa.bottom < wysokość:
                platforma_lewa.y += prędkość_platform
            ruch_si(platforma_prawa, piłka, poziom_trudności)
        else:
            if klawisze[pygame.K_UP] and platforma_prawa.top > 0:
                platforma_prawa.y -= prędkość_platform
            if klawisze[pygame.K_DOWN] and platforma_prawa.bottom < wysokość:
                platforma_prawa.y += prędkość_platform
            ruch_si(platforma_lewa, piłka, poziom_trudności)

    # Ruch piłki
    nowa_pozycja_x = piłka.x + piłka_dx
    nowa_pozycja_y = piłka.y + piłka_dy

    # Tworzenie prostokąta reprezentującego nową pozycję piłki
    nowa_piłka = pygame.Rect(nowa_pozycja_x, nowa_pozycja_y, piłka.width, piłka.height)

    # Sprawdzenie kolizji z platformami
    if nowa_piłka.colliderect(platforma_lewa):
        odbij_od_platformy(platforma_lewa)
    elif nowa_piłka.colliderect(platforma_prawa):
        odbij_od_platformy(platforma_prawa)
    else:
        # Sprawdzenie kolizji ze ścianami
        if nowa_pozycja_y <= 0 or nowa_pozycja_y + piłka.height >= wysokość:
            odbij_od_ściany()
        elif nowa_pozycja_x <= 0 or nowa_pozycja_x + piłka.width >= szerokość:
            odbij_od_bocznej_ściany()
        else:
            piłka.x = nowa_pozycja_x
            piłka.y = nowa_pozycja_y

    # Przyznawanie punktów i resetowanie piłki tylko gdy trafi w bramkę
    if piłka.colliderect(bramka_lewa):
        punkty_prawy += 1
        resetuj_piłkę()
    elif piłka.colliderect(bramka_prawa):
        punkty_lewy += 1
        resetuj_piłkę()

    # Sprawdzenie czy któryś z graczy osiągnął maksymalną liczbę punktów
    if punkty_lewy == MAX_PUNKTY:
        wyświetl_zwycięzcę("Lewy gracz")
        punkty_lewy = 0
        punkty_prawy = 0
        czas_początkowy = time.time()
    elif punkty_prawy == MAX_PUNKTY:
        wyświetl_zwycięzcę("Prawy gracz")
        punkty_lewy = 0
        punkty_prawy = 0
        czas_początkowy = time.time()

    # Rysowanie
    rysuj_tło()
    pygame.draw.rect(okno, CZARNY, platforma_lewa)
    pygame.draw.rect(okno, CZARNY, platforma_prawa)
    pygame.draw.ellipse(okno, POMARAŃCZOWY, piłka)
    pygame.draw.rect(okno, NIEBIESKI, bramka_lewa)
    pygame.draw.rect(okno, CZERWONY, bramka_prawa)

    # Wyświetlanie punktów
    tekst_lewy = czcionka.render(str(punkty_lewy), True, NIEBIESKI)
    tekst_prawy = czcionka.render(str(punkty_prawy), True, CZERWONY)
    okno.blit(tekst_lewy, (szerokość//4, 20))
    okno.blit(tekst_prawy, (3*szerokość//4, 20))

    # Wyświetlanie prędkości piłki
    tekst_prędkość = czcionka.render(f"Prędkość: {piłka_prędkość:.1f}", True, CZARNY)
    okno.blit(tekst_prędkość, (szerokość//2 - 70, 20))

    # Wyświetlanie timera
    tekst_czas = czcionka.render(f"Czas: {czas_gry}s", True, CZARNY)
    okno.blit(tekst_czas, (szerokość//2 - 50, 50))

    pygame.display.flip()
    zegar.tick(60)
