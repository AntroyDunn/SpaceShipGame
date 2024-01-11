# -*- coding: utf-8 -*-
"""
Created on Wed 10/01/2024

@author: CouryDunn
"""

import pygame
import os


#dimesions of the game window
WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BULLETS_VEL = 7

MAX_BULLETS = 20

pygame.display.set_caption("Shooting Ships Game")

WHITE = (255, 255, 255)

ORANGE = (200, 100, 100)

BLACK = (10, 10, 10)

BORDER = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

FPS = 75

VEL = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

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
def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, ORANGE, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, ORANGE, bullet)
    
    pygame.display.update()

def red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 10: #left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #Right
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 5: #down
            red.y += VEL

def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 5: #down
            yellow.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))            
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))            
            red_bullets.remove(bullet) 

#Clock controls the speed of the while loop how many frames per second are running 6 cap
#this is for quiting the game
def main():
    red = pygame.Rect(700, 150, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
    yellow = pygame.Rect(100, 150, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_END and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_e and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x - red.width, red.y + yellow.height//2 -2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        
        yellow_movement(keys_pressed, yellow)
        
        red_movement(keys_pressed, red)
        
        draw_window(red, yellow, red_bullets, yellow_bullets)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

    pygame.quit()
#runs this file directly not it imported from somewhere else
if __name__ == "__main__":
    main()                
