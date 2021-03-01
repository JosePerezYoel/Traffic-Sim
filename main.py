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

def main():

    timer = 0
    running = True
    spawnRate = random.randint(1, 10) # Chooses the first rate the cars will spawn, will be changed later
    cars = []
    voidCars = []
    car_x = [315, 377, 440, 535, 597, 660]
    car_y = [-100, 1100]
    while running:
        timer += 1

        screen.blit(ROAD, (0, 0))

        if timer > 120:  # Every one to ten seconds
            spawnRate = random.randint(1,10) # Rerolls for another spawnRate, this is so that the cars dont spawn in a uniform rate
            timer = 0 # Resets the timer
            cars.append(c.Car(315, 0))
            cars.append(c.Car(377, 0))
            cars.append(c.Car(440, 0))
            cars.append(c.Car(525, 1000))
            cars.append(c.Car(597, 1000))
            cars.append(c.Car(660, 1000))



        for car in cars:
            car.render(screen)
            car.move()
            if car.y > 1000 or car.y < -100:
                voidCars.append(car)
        for voidCar in voidCars:
            for car in cars:
                if car == voidCar:
                    cars.remove(car)

        voidCars.clear()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                print(cars)
                print(voidCars)
        pygame.display.flip()
        clock.tick(60)

main()


