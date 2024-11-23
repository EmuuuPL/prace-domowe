import pygame
import sys
from enum import Enum
from typing import Optional, Tuple, List
import random

class GameState(Enum):
    MENU = 0
    DIFFICULTY = 1  # Nowy stan dla menu trudności
    PLAYING = 2
    GAME_OVER = 3

class GameMode(Enum):
    ONE_PLAYER = 0
    TWO_PLAYERS = 1

class Difficulty(Enum):
    EASY = 0
    HARD = 1

class Player(Enum):
    X = "X"
    O = "O"

class Colors:
    BG = (28, 170, 156)
    LINE = (23, 145, 135)
    CIRCLE = (239, 231, 200)
    CROSS = (66, 66, 66)
    TEXT = (255, 255, 255)
    WIN_LINE = (255, 70, 70)

class GameConfig:
    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    BOARD_SIZE = 3
    SQUARE_SIZE = WIDTH // BOARD_SIZE
    CIRCLE_RADIUS = SQUARE_SIZE // 3
    CROSS_WIDTH = 25
    SPACE = SQUARE_SIZE // 4
    FPS = 60

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.WIDTH, GameConfig.HEIGHT))
        pygame.display.set_caption("Kółko i Krzyżyk")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        
        self.game_state = GameState.MENU
        self.game_mode = None
        self.difficulty = None
        self.board = self._create_empty_board()
        self.current_player = Player.X
        self.winner = None
        self.winning_line = None

    def _create_empty_board(self) -> List[List[str]]:
        return [[" " for _ in range(GameConfig.BOARD_SIZE)] for _ in range(GameConfig.BOARD_SIZE)]

    def draw_menu(self) -> None:
        self.screen.fill(Colors.BG)
        title = self.font.render("Kółko i Krzyżyk", True, Colors.TEXT)
        one_player = self.font.render("1 - Jeden Gracz", True, Colors.TEXT)
        two_players = self.font.render("2 - Dwóch Graczy", True, Colors.TEXT)
        
        self.screen.blit(title, (GameConfig.WIDTH//2 - title.get_width()//2, 150))
        self.screen.blit(one_player, (GameConfig.WIDTH//2 - one_player.get_width()//2, 250))
        self.screen.blit(two_players, (GameConfig.WIDTH//2 - two_players.get_width()//2, 350))

    def draw_difficulty_menu(self) -> None:
        self.screen.fill(Colors.BG)
        title = self.font.render("Wybierz poziom trudności", True, Colors.TEXT)
        easy = self.font.render("1 - Łatwy", True, Colors.TEXT)
        hard = self.font.render("2 - Trudny", True, Colors.TEXT)
        
        self.screen.blit(title, (GameConfig.WIDTH//2 - title.get_width()//2, 150))
        self.screen.blit(easy, (GameConfig.WIDTH//2 - easy.get_width()//2, 250))
        self.screen.blit(hard, (GameConfig.WIDTH//2 - hard.get_width()//2, 350))

    def draw_board(self) -> None:
        self.screen.fill(Colors.BG)
        # Linie pionowe
        for i in range(1, GameConfig.BOARD_SIZE):
            pygame.draw.line(
                self.screen, Colors.LINE,
                (i * GameConfig.SQUARE_SIZE, 0),
                (i * GameConfig.SQUARE_SIZE, GameConfig.HEIGHT),
                GameConfig.LINE_WIDTH
            )
        # Linie poziome
        for i in range(1, GameConfig.BOARD_SIZE):
            pygame.draw.line(
                self.screen, Colors.LINE,
                (0, i * GameConfig.SQUARE_SIZE),
                (GameConfig.WIDTH, i * GameConfig.SQUARE_SIZE),
                GameConfig.LINE_WIDTH
            )

    def draw_figures(self) -> None:
        for row in range(GameConfig.BOARD_SIZE):
            for col in range(GameConfig.BOARD_SIZE):
                if self.board[row][col] == Player.X.value:
                    self._draw_cross(row, col)
                elif self.board[row][col] == Player.O.value:
                    self._draw_circle(row, col)

    def _draw_cross(self, row: int, col: int) -> None:
        start_desc = (col * GameConfig.SQUARE_SIZE + GameConfig.SPACE,
                     row * GameConfig.SQUARE_SIZE + GameConfig.SPACE)
        end_desc = (col * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE - GameConfig.SPACE,
                   row * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE - GameConfig.SPACE)
        start_asc = (col * GameConfig.SQUARE_SIZE + GameConfig.SPACE,
                    row * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE - GameConfig.SPACE)
        end_asc = (col * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE - GameConfig.SPACE,
                  row * GameConfig.SQUARE_SIZE + GameConfig.SPACE)
        
        pygame.draw.line(self.screen, Colors.CROSS, start_desc, end_desc, GameConfig.CROSS_WIDTH)
        pygame.draw.line(self.screen, Colors.CROSS, start_asc, end_asc, GameConfig.CROSS_WIDTH)

    def _draw_circle(self, row: int, col: int) -> None:
        center = (col * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2,
                 row * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2)
        pygame.draw.circle(self.screen, Colors.CIRCLE, center, GameConfig.CIRCLE_RADIUS, GameConfig.LINE_WIDTH)

    def draw_game_over(self) -> None:
        if self.winning_line:
            start_pos, end_pos = self.winning_line
            pygame.draw.line(self.screen, Colors.WIN_LINE, 
                           start_pos, end_pos, GameConfig.LINE_WIDTH)
        
        text = "Remis!" if not self.winner else f"Wygrywa {self.winner}!"
        surface = self.font.render(text, True, Colors.TEXT)
        restart_text = self.font.render("Naciśnij SPACJĘ aby zagrać ponownie", True, Colors.TEXT)
        menu_text = self.font.render("ESC - Powrót do menu", True, Colors.TEXT)
        
        self.screen.blit(surface, 
                        (GameConfig.WIDTH//2 - surface.get_width()//2, 20))
        self.screen.blit(restart_text,
                        (GameConfig.WIDTH//2 - restart_text.get_width()//2, 
                         GameConfig.HEIGHT - 100))
        self.screen.blit(menu_text,
                        (GameConfig.WIDTH//2 - menu_text.get_width()//2, 
                         GameConfig.HEIGHT - 50))

    def check_winner(self) -> Optional[str]:
        # Sprawdzenie wierszy
        for row in range(GameConfig.BOARD_SIZE):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winning_line = (
                    (0, row * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2),
                    (GameConfig.WIDTH, row * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2)
                )
                return self.board[row][0]

        # Sprawdzenie kolumn
        for col in range(GameConfig.BOARD_SIZE):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winning_line = (
                    (col * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2, 0),
                    (col * GameConfig.SQUARE_SIZE + GameConfig.SQUARE_SIZE // 2, GameConfig.HEIGHT)
                )
                return self.board[0][col]

        # Sprawdzenie przekątnych
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winning_line = ((0, 0), (GameConfig.WIDTH, GameConfig.HEIGHT))
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winning_line = ((GameConfig.WIDTH, 0), (0, GameConfig.HEIGHT))
            return self.board[0][2]

        return None

    def is_board_full(self) -> bool:
        return all(cell != " " for row in self.board for cell in row)

    def make_ai_move(self) -> None:
        if self.difficulty == Difficulty.EASY:
            self._make_random_move()
        else:
            self._make_smart_move()

    def _make_random_move(self) -> None:
        empty_cells = [(r, c) for r in range(GameConfig.BOARD_SIZE) 
                      for c in range(GameConfig.BOARD_SIZE) if self.board[r][c] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.current_player.value

    def _make_smart_move(self) -> None:
        # Najpierw sprawdź możliwość wygranej
        if self._try_winning_move():
            return
        
        # Jeśli nie ma możliwości wygranej, zablokuj przeciwnika
        if self._try_blocking_move():
            return
        
        # Jeśli nie ma możliwości blokady, zajmij środek planszy
        if self.board[1][1] == " ":
            self.board[1][1] = self.current_player.value
            return
        
        # W przeciwnym razie wykonaj losowy ruch
        self._make_random_move()

    def _try_winning_move(self) -> bool:
        return self._try_strategic_move(self.current_player.value)

    def _try_blocking_move(self) -> bool:
        opponent = Player.O if self.current_player == Player.X else Player.X
        return self._try_strategic_move(opponent.value)

    def _try_strategic_move(self, player: str) -> bool:
        for row in range(GameConfig.BOARD_SIZE):
            for col in range(GameConfig.BOARD_SIZE):
                if self.board[row][col] == " ":
                    self.board[row][col] = player
                    if self.check_winner() == player:
                        if player != self.current_player.value:
                            self.board[row][col] = self.current_player.value
                        return True
                    self.board[row][col] = " "
        return False

    def reset_game(self) -> None:
        self.board = self._create_empty_board()
        self.current_player = Player.X
        self.winner = None
        self.winning_line = None

    def return_to_menu(self) -> None:
        self.game_state = GameState.MENU
        self.game_mode = None
        self.difficulty = None
        self.reset_game()

    def handle_click(self, pos: Tuple[int, int]) -> None:
        if self.game_state != GameState.PLAYING:
            return

        col = pos[0] // GameConfig.SQUARE_SIZE
        row = pos[1] // GameConfig.SQUARE_SIZE
        
        if 0 <= row < GameConfig.BOARD_SIZE and 0 <= col < GameConfig.BOARD_SIZE:
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player.value
                self.winner = self.check_winner()
                
                if self.winner or self.is_board_full():
                    self.game_state = GameState.GAME_OVER
                else:
                    self.current_player = Player.O if self.current_player == Player.X else Player.X
                    
                    # Wykonaj ruch SI jeśli jest tryb jednoosobowy i jest tura komputera
                    if (self.game_mode == GameMode.ONE_PLAYER and 
                        self.current_player == Player.O):
                        pygame.display.flip()  # Odśwież ekran przed ruchem SI
                        pygame.time.wait(500)  # Poczekaj chwilę przed ruchem SI
                        self.make_ai_move()
                        self.winner = self.check_winner()
                        if self.winner or self.is_board_full():
                            self.game_state = GameState.GAME_OVER
                        else:
                            self.current_player = Player.X

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.game_state == GameState.PLAYING or self.game_state == GameState.GAME_OVER:
                            self.return_to_menu()
                        else:
                            running = False
                    elif event.key == pygame.K_SPACE and self.game_state == GameState.GAME_OVER:
                        self.reset_game()
                        self.game_state = GameState.PLAYING
                    elif self.game_state == GameState.MENU:
                        if event.key == pygame.K_1:
                            self.game_mode = GameMode.ONE_PLAYER
                            self.game_state = GameState.DIFFICULTY
                        elif event.key == pygame.K_2:
                            self.game_mode = GameMode.TWO_PLAYERS
                            self.game_state = GameState.PLAYING
                    elif self.game_state == GameState.DIFFICULTY:
                        if event.key == pygame.K_1:
                            self.difficulty = Difficulty.EASY
                            self.game_state = GameState.PLAYING
                        elif event.key == pygame.K_2:
                            self.difficulty = Difficulty.HARD
                            self.game_state = GameState.PLAYING
                elif event.type == pygame.MOUSEBUTTONDOWN and self.game_state == GameState.PLAYING:
                    self.handle_click(event.pos)

            # Rysowanie odpowiedniego ekranu
            if self.game_state == GameState.MENU:
                self.draw_menu()
            elif self.game_state == GameState.DIFFICULTY:
                self.draw_difficulty_menu()
            elif self.game_state == GameState.PLAYING:
                self.draw_board()
                self.draw_figures()
            elif self.game_state == GameState.GAME_OVER:
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(GameConfig.FPS)

if __name__ == "__main__":
    game = TicTacToe()
    game.run()