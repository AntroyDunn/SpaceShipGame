# -*- coding: utf-8 -*-
"""
Created on Wed 10/01/2024

@author: CouryDunn
"""

import pygame
import os

#After Git

#dimesions of the game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Ships Game")

BLUE = (30, 10, 221)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 54, 44

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


#order in which we draw things matters
def draw_window(red, yellow):
    WIN.fill(BLUE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT]: #left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: #Right
            red.x += VEL
        if keys_pressed[pygame.K_UP]: #up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]: #down
            red.y += VEL

def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a]: #left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: #Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: #up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]: #down
            yellow.y += VEL


#Clock controls the speed of the while loop how many frames per second are running 6 cap
#this is for quiting the game
def main():
    red = pygame.Rect(700, 150, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
    yellow = pygame.Rect(100, 150, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()
#runs this file directly not it imported from somewhere else
if __name__ == "__main__":
    main()                
