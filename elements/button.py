import pygame

from configs import ColorConfig


class Button(object):

    def __init__(self, x_coordinate: int, y_coordinate: int, button_width: int,
                 button_height: int, text_font: str, text_size: str,
                 button_name: str, onclick_function=None):
        self.x = x_coordinate
        self.y = y_coordinate
        self.width = button_width
        self.height = button_height
        self.function_by_click = onclick_function
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pygame.font.SysFont(
            text_font, int(text_size)).render(button_name, True, (20, 20, 20))

    def process(self, game_window: pygame.display, parameter: str):
        self.buttonSurface.fill(ColorConfig.WHITE)
        if self.buttonRect.collidepoint(pygame.mouse.get_pos()):
            self.buttonSurface.fill(ColorConfig.GREY)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(ColorConfig.GREEN)
                self.function_by_click(parameter)
                return True
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        game_window.blit(self.buttonSurface, self.buttonRect)
