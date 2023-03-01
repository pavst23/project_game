import time
from copy import deepcopy
from datetime import datetime

import pygame

from configs import ColorConfig
from configs import GameConfig
from configs import TextConfig
from configs import WindowConfig
from json_manager import JSONResults


class GameFunctions(object):

    @classmethod
    def show_main_menu(cls):
        pass

    @classmethod
    def show_score(cls, game_window: pygame.display, score: int,
                   color: pygame.Color, font: str, size: int, name: str):
        surface = pygame.font.SysFont(font, size).render(
            f"Score of {name} player: {score}", True, color)
        game_window.blit(surface, surface.get_rect())

    @classmethod
    def check_game_win(cls, snake_body: list):
        if len(snake_body) >= (WindowConfig.WINDOW_WIDTH // 10) * (
                WindowConfig.WINDOW_HEIGHT // 10):
            return True
        else:
            return False

    @classmethod
    def show_game_win_text(cls, game_window: pygame.display, score: int,
                           color: pygame.Color, font: str, size: int):
        surface = pygame.font.SysFont(font, size).render(
            f"YOU WIN! SCORE IS: {score}", True, color)
        rect = surface.get_rect()
        rect.midtop = (WindowConfig.WINDOW_WIDTH / 2,
                       WindowConfig.WINDOW_HEIGHT / 2)
        game_window.blit(surface, rect)
        pygame.display.flip()

    @classmethod
    def show_game_over_text(cls, game_window: pygame.display, score: int,
                            color: pygame.Color, font: str, size: int):
        surface = pygame.font.SysFont(font, size).render(
            f"GAME OVER! YOUR SCORE IS: {score}", True, color)
        rect = surface.get_rect()
        rect.midtop = (WindowConfig.WINDOW_WIDTH / 2,
                       WindowConfig.WINDOW_HEIGHT / 2)
        game_window.blit(surface, rect)
        pygame.display.flip()
        time.sleep(2)
        game_window.fill(ColorConfig.BLACK)
        cls.draw_results(game_window=game_window, font=TextConfig.MAIN_FONT,
                         size=TextConfig.SCORE_FONT_SIZE,
                         color=ColorConfig.WHITE)
        pygame.quit()
        quit()

    @classmethod
    def results_appending(cls, result: int, name: str):
        results = JSONResults()
        results_dict = results.get_results()
        results_num_flag = False
        if len(results_dict.items()) == 5:
            results_num_flag = True
        dict_copy = deepcopy(results_dict)
        timestamp = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        for key, value in dict_copy.items():
            if value < result and results_num_flag:
                new_key = timestamp + " " + name
                results_dict.pop(list(dict_copy.items())[-1][0])
                results_dict[new_key] = result
                break
            elif value < result:
                new_key = timestamp + "   " + name
                results_dict[new_key] = result
                break
        sorted_results_dict = \
            dict(sorted(results_dict.items(), key=lambda item: item[1],
                        reverse=True))
        if results_num_flag:
            results.save_result(data=sorted_results_dict, rewrite_flag=True)
        else:
            results.save_result(data=sorted_results_dict)

    @classmethod
    def draw_results(cls, game_window: pygame.display, font: str, size: int,
                     color: pygame.Color):

        position = (WindowConfig.WINDOW_WIDTH / 8,
                    WindowConfig.WINDOW_HEIGHT / 8)
        results = JSONResults()
        labels = []
        labels.append(pygame.font.SysFont(font, size).render(
            "RESULT TABLE:", True, color))
        for key, value in results.get_results().items():
            line = f"{key}:  {value}"
            labels.append(pygame.font.SysFont(font, size).render(
                line, True, color))
        for line in range(len(labels)):
            game_window.blit(labels[line], (position[0], position[1] +
                                            (line * size) + (15 * line)))
            pygame.display.flip()
            time.sleep(1)

    @staticmethod
    def change_difficulty(difficulty: str):
        options = GameConfig.DIFFICULTY_LEVELS[difficulty]
        GameConfig.GAME_SPEED = options["speed"]
        GameConfig.GAME_SPEED_DELTA = options["speed_delta"]
