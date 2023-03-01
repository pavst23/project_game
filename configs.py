import pygame


class WindowConfig(object):

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480


class ColorConfig(object):

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    BLUE = pygame.Color(0, 0, 255)
    GREEN = pygame.Color(0, 255, 0)
    RED = pygame.Color(255, 0, 0)
    GREY = pygame.Color(128, 128, 128)


class GameConfig(object):

    GAME_TITLE = "Reversible Sssnake!"
    DEFAULT_GAME_SCORE = 0
    DEFAULT_SNAKE_POSITION = [WindowConfig.WINDOW_WIDTH // 2,
                              WindowConfig.WINDOW_HEIGHT // 2]
    SNAKE_BODY = [[(WindowConfig.WINDOW_WIDTH // 2 - 10 * i),
                   WindowConfig.WINDOW_HEIGHT // 2] for i in range(5)]
    DEFAULT_SNAKE_DIRECTION = "UP"
    GAME_SPEED = 5
    GAME_SPEED_DELTA = 1
    DEFAULT_FRUIT_FLAG = True
    POSSIBLE_DEFAULT_FRUIT_POSITIONS = [
        [WindowConfig.WINDOW_WIDTH // 4, WindowConfig.WINDOW_HEIGHT // 4],
        [WindowConfig.WINDOW_WIDTH - WindowConfig.WINDOW_WIDTH // 4,
         WindowConfig.WINDOW_HEIGHT // 4],
        [WindowConfig.WINDOW_WIDTH // 4, WindowConfig.WINDOW_HEIGHT -
         WindowConfig.WINDOW_HEIGHT // 4],
        [WindowConfig.WINDOW_WIDTH - WindowConfig.WINDOW_WIDTH // 4,
         WindowConfig.WINDOW_HEIGHT - WindowConfig.WINDOW_HEIGHT // 4]
    ]
    DIFFICULTY_LEVELS = {"easy": {"speed": 2, "speed_delta": 0.5},
                         "medium": {"speed": 5, "speed_delta": 1},
                         "snake": {"speed": 8, "speed_delta": 2}}


class TextConfig(object):

    MAIN_FONT = "comicsansms"
    SCORE_FONT_SIZE = WindowConfig.WINDOW_WIDTH // 25
    MAIN_FONT_SIZE = WindowConfig.WINDOW_WIDTH // 20


class ResultsFileConfig(object):

    FILENAME = "results.json"


class DifficultyButtonsConfig(object):

    EASY_BUTTON = [WindowConfig.WINDOW_WIDTH // 3,
                   WindowConfig.WINDOW_HEIGHT // 3,
                   WindowConfig.WINDOW_WIDTH // 3,
                   WindowConfig.WINDOW_HEIGHT // 9,
                   TextConfig.MAIN_FONT, TextConfig.MAIN_FONT_SIZE,
                   "EASY"]
    MEDIUM_BUTTON = [WindowConfig.WINDOW_WIDTH // 3,
                     WindowConfig.WINDOW_HEIGHT // 3 + 80,
                     WindowConfig.WINDOW_WIDTH // 3,
                     WindowConfig.WINDOW_HEIGHT // 9,
                     TextConfig.MAIN_FONT,
                     TextConfig.MAIN_FONT_SIZE,
                     "MEDIUM"]
    SNAKE_BUTTON = [WindowConfig.WINDOW_WIDTH // 3,
                    WindowConfig.WINDOW_HEIGHT // 3 + 160,
                    WindowConfig.WINDOW_WIDTH // 3,
                    WindowConfig.WINDOW_HEIGHT // 9,
                    TextConfig.MAIN_FONT, TextConfig.MAIN_FONT_SIZE,
                    "SNAKE"]
    BUTTONS_LIST = [EASY_BUTTON, MEDIUM_BUTTON, SNAKE_BUTTON]
