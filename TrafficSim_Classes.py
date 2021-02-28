import pygame
import random
pygame.init()


class GameManager:
    def __init__(self):
        pass


class Car:


    def __init__(self, x, y, skill = 0):  # Skill is how likely that the car will NOT make mistakes
        BLUE = 0, 255, 0
        RED = 255, 0, 0
        GREEN = 0, 0, 255
        colors = [BLUE, RED, GREEN]
        self.skill = skill
        self.x = x
        self.y = y
        self.start_y = y
        self.color = random.choice(colors)
        self.speed = random.randint(4,10)


    def get_rect(self):
        return pygame.rect.Rect(self.x, self.y, 25, 50)


    def move(self):
        if self.start_y > 500:
            self.y += -self.speed
        elif self.start_y < 500:
            self.y += self.speed


    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())


