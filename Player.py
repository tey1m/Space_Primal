import pygame
import Map as mp


class Player:
    def __init__(self, width, height, x, y, camera_x, camera_y, player_x, player_y, speed):
        self.x = x
        self.y = y
        self.camera_x = camera_x
        self.camera_y = camera_y
        self.player_x = player_x
        self.player_y = player_y
        self.speed = speed

        self.map = mp.Map(width, height, 32, 50, 50)

    def move(self, pressed_key):
        speed = self.speed + 0.6
        if pressed_key == pygame.K_LEFT:
            self.camera_x += speed
            self.camera_y += speed / 2
            self.player_x -= self.speed
            self.player_y -= self.speed / 2
        elif pressed_key == pygame.K_RIGHT:
            self.camera_x -= speed
            self.camera_y -= speed / 2
            self.player_x += self.speed
            self.player_y += self.speed / 2
        elif pressed_key == pygame.K_UP:
            self.camera_y += speed / 2
            self.camera_x -= speed
            self.player_y -= self.speed / 2
            self.player_x += self.speed
        elif pressed_key == pygame.K_DOWN:
            self.camera_y -= speed / 2
            self.camera_x += speed
            self.player_y += self.speed / 2
            self.player_x -= self.speed
