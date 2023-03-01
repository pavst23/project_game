import pygame
import random
from copy import copy

from configs import ColorConfig, GameConfig, TextConfig, WindowConfig, \
    DifficultyButtonsConfig
from elements.button import Button
from game_functions import GameFunctions
from game_mechanics import GameMechanics


print("Welcome to the reversible snake game")
name = input("Enter your name: ")

pygame.init()

pygame.display.set_caption(GameConfig.GAME_TITLE)
game_window = pygame.display.set_mode((WindowConfig.WINDOW_WIDTH,
                                       WindowConfig.WINDOW_HEIGHT))
fps = pygame.time.Clock()
snake_direction = GameConfig.DEFAULT_SNAKE_DIRECTION
snake_position = GameConfig.DEFAULT_SNAKE_POSITION
fruit_position = GameConfig.POSSIBLE_DEFAULT_FRUIT_POSITIONS[
    random.randrange(4)]
snake_body = GameConfig.SNAKE_BODY
fruit_position_flag = GameConfig.DEFAULT_FRUIT_FLAG
game_score = GameConfig.DEFAULT_GAME_SCORE

for elem in DifficultyButtonsConfig.BUTTONS_LIST:
    elem.append(GameFunctions.change_difficulty)

easy_button = Button(*DifficultyButtonsConfig.EASY_BUTTON)
medium_button = Button(*DifficultyButtonsConfig.MEDIUM_BUTTON)
snake_button = Button(*DifficultyButtonsConfig.SNAKE_BUTTON)
buttons_list = [easy_button, medium_button, snake_button]

difficulty_flag = True
while difficulty_flag:

    game_window.fill(ColorConfig.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for button, parameter in zip(buttons_list, list(
            GameConfig.DIFFICULTY_LEVELS.keys())):
        res = button.process(game_window=game_window, parameter=parameter)
        if res:
            buttons_list = []
            difficulty_flag = False
            break
    pygame.display.update()
    fps.tick(GameConfig.GAME_SPEED)

game_window.fill(ColorConfig.BLACK)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            break

    snake_position = GameMechanics.snake_move(
        snake_direction=snake_direction, snake_position=snake_position)
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and \
            snake_position[1] == fruit_position[1]:
        fruit_position_flag = True
        game_score += 1
        while fruit_position_flag:
            fruit_position = GameMechanics.generate_new_fruit_position()
            if fruit_position not in snake_body:
                fruit_position_flag = False
        snake_body.reverse()
        snake_position = copy(snake_body[0])
        snake_direction = GameMechanics.change_direction_to_opposite(
            snake_body=snake_body)
        GameConfig.GAME_SPEED += GameConfig.GAME_SPEED_DELTA
    else:
        snake_body.pop()

    game_window.fill(ColorConfig.BLACK)

    for pos in snake_body:
        pygame.draw.rect(game_window, ColorConfig.WHITE,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, ColorConfig.BLUE, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    border_touch_flag = False
    if (snake_position[0] < 0 or snake_position[0] >
            WindowConfig.WINDOW_WIDTH - 10) or \
            (snake_position[1] < 0 or snake_position[1] >
             WindowConfig.WINDOW_HEIGHT - 10):
        border_touch_flag = True

    snake_body_touch_flag = False
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            snake_body_touch_flag = True
            break

    if border_touch_flag or snake_body_touch_flag:
        GameFunctions.results_appending(result=game_score, name=name)
        GameFunctions.show_game_over_text(
            game_window=game_window, score=game_score,
            color=ColorConfig.RED, font=TextConfig.MAIN_FONT,
            size=TextConfig.MAIN_FONT_SIZE
        )

    GameFunctions.show_score(
        game_window=game_window, score=game_score,
        color=ColorConfig.WHITE, font=TextConfig.MAIN_FONT,
        size=TextConfig.SCORE_FONT_SIZE, name=name
    )

    if GameFunctions.check_game_win(snake_body=snake_body):
        GameFunctions.show_game_win_text(
            game_window=game_window, score=game_score,
            color=ColorConfig.WHITE, font=TextConfig.MAIN_FONT,
            size=TextConfig.MAIN_FONT_SIZE
        )
        GameFunctions.results_appending(result=game_score, name=name)
        pygame.quit()
        quit()

    pygame.display.update()
    fps.tick(GameConfig.GAME_SPEED)
