import pygame
import random
import sys

# Inicjalizacja pygame
pygame.init()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ustawienia ekranu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Segregowanie Śmieci")

# Załadowanie obrazków (zastąp nazwami plików z grafikami śmieci i pojemników)
# Przykładowe kształty reprezentujące pojemniki
TRASH_BIN_COLORS = {
    "plastik": (255, 255, 0),    # żółty
    "papier": (0, 0, 255),       # niebieski
    "bio": (0, 255, 0),          # zielony
    "szkło": (255, 0, 0),        # czerwony
    "metal": (128, 128, 128)     # szary
}

# Lista śmieci i pojemników
smieci = [
    {"name": "butelka plastikowa", "type": "plastik"},
    {"name": "gazeta", "type": "papier"},
    {"name": "skórka od banana", "type": "bio"},
    {"name": "słoik", "type": "szkło"},
    {"name": "puszka aluminiowa", "type": "metal"},
    {"name": "opakowanie po jogurcie", "type": "plastik"},
    {"name": "karton po mleku", "type": "papier"},
    {"name": "resztki jedzenia", "type": "bio"},
    {"name": "butelka szklana", "type": "szkło"},
    {"name": "puszka po napoju", "type": "metal"},
    {"name": "opakowanie po chipsach", "type": "plastik"},
    {"name": "stara książka", "type": "papier"},
]

# Pozycje pojemników na ekranie
bins_positions = {
    "plastik": (50, 400),
    "papier": (200, 400),
    "bio": (350, 400),
    "szkło": (500, 400),
    "metal": (650, 400)
}

# Zmienna wyników
punkty = 0

# Funkcja do wyświetlania tekstu na ekranie
font = pygame.font.Font(None, 36)
def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Funkcja do rysowania prostokąta i tekstu
def draw_rect_with_text(color, rect, text, text_color=BLACK):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 5, rect.y + 15, text_color)

# Funkcja główna gry
def main():
    global punkty
    running = True
    selected_trash = random.choice(smieci)
    selected_trash_position = (SCREEN_WIDTH // 2, 50)
    trash_dragging = False

    while running:
        screen.fill(WHITE)
        
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(selected_trash_position[0], selected_trash_position[1], 150, 75).collidepoint(event.pos):
                    trash_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                trash_dragging = False
                for bin_type, pos in bins_positions.items():
                    bin_rect = pygame.Rect(pos[0], pos[1], 100, 100)
                    if bin_rect.collidepoint(event.pos):
                        if bin_type == selected_trash["type"]:
                            punkty += 1  # Dodaj punkt za poprawne wrzucenie
                        else:
                            punkty -= 1  # Odejmij punkt za błędne wrzucenie
                        selected_trash = random.choice(smieci)
                        selected_trash_position = (SCREEN_WIDTH // 2, 50)
                        break
            elif event.type == pygame.MOUSEMOTION and trash_dragging:
                selected_trash_position = event.pos

        # Rysowanie pojemników
        for bin_type, pos in bins_positions.items():
            draw_rect_with_text(TRASH_BIN_COLORS[bin_type], pygame.Rect(pos[0], pos[1], 100, 100), bin_type)

        # Rysowanie śmieci
        text_surface = font.render(selected_trash["name"], True, WHITE)  # Renderowanie tekstu
        text_width, text_height = text_surface.get_size()  # Pobranie rozmiaru tekstu
        trash_rect = pygame.Rect(selected_trash_position[0], selected_trash_position[1], text_width + 10, text_height + 10)  # Ustawienie prostokąta na podstawie rozmiaru tekstu
        pygame.draw.rect(screen, BLACK, trash_rect)  # Rysowanie prostokąta
        draw_text(selected_trash["name"], selected_trash_position[0] + 5, selected_trash_position[1] + 5, WHITE)  # Rysowanie tekstu

        # Wyświetlanie punktacji
        draw_text(f"Punkty: {punkty}", 10, 10, BLACK)

        # Aktualizacja ekranu
        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Uruchomienie gry
if __name__ == "__main__":
    main()
