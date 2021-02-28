import pygame
from pygame.locals import *
import TrafficSim_Classes as c
import random

pygame.init()
clock = pygame.time.Clock()


WIN_WIDTH = 1000
WIN_HEIGHT = 1000
WINDOW_SIZE = WIN_WIDTH, WIN_HEIGHT  # I know I can use WIDTH for both values but I like it like this better

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Traffic Simulation")

BLACK = 0, 0, 0

ROAD = pygame.image.load("Art/Road.png")

testCar = c.Car(580, 0)

def get_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
def spawn_cars():
    cars = []














def main():
    testCar = c.Car(315, 1000)
    timer = 0
    running = True
    spawnRate = random.randint(1, 10) # Chooses the first rate the cars will spawn, will be changed later
    cars = []
    car_x = [315, 377, 440, 535, 597, 660]
    car_y = [-100, 1100]
    while running:
        timer += 1


        screen.fill(BLACK)
        screen.blit(ROAD, (0, 0))

        if timer > spawnRate * 60:  # Every one to ten seconds
            spawnRate = random.randint(1,10) # Rerolls for another spawnRate, this is so that the cars dont spawn in a uniform rate
            timer = 0 # Resets the timer
            for x in range(5):

                cars.append(c.Car(random.choice(car_x), random.choice(car_y)))


        for car in cars:
            car.render(screen)
            car.move(2)






        get_events()
        pygame.display.flip()
        clock.tick(60)

main()


