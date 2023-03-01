import random

from configs import WindowConfig


class GameMechanics(object):

    @classmethod
    def snake_move(cls, snake_direction: str, snake_position: list):
        if snake_direction == "UP":
            snake_position[1] -= 10
        if snake_direction == "DOWN":
            snake_position[1] += 10
        if snake_direction == "LEFT":
            snake_position[0] -= 10
        if snake_direction == "RIGHT":
            snake_position[0] += 10
        return snake_position

    @classmethod
    def generate_new_fruit_position(cls):
        return [random.randrange(1, WindowConfig.WINDOW_WIDTH // 10) * 10,
                random.randrange(1, WindowConfig.WINDOW_HEIGHT // 10) * 10]

    @staticmethod
    def change_direction_to_opposite(snake_body: list):
        if snake_body[0][0] > snake_body[1][0]:
            return "RIGHT"
        elif snake_body[0][0] < snake_body[1][0]:
            return "LEFT"
        elif snake_body[0][1] > snake_body[1][1]:
            return "DOWN"
        else:
            return "UP"
