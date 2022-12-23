import pygame
import numpy as np
import random


# WIDTH = 640
# HEIGHT = 480
# TILE_SIZE = 32
# X_GRID_COUNT = 40
# Y_GRID_COUNT = 40


# Window dimensions
class Map:

    def __init__(self, width, height, tile_size, x_grid_count, y_grid_count):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.x_grid_count = x_grid_count
        self.y_grid_count = y_grid_count

        # Initialize Pygame
        pygame.init()

        # Set up the window
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Load the images
        self.grass = pygame.image.load("images/ground.png")
        self.tree = pygame.image.load("images/tree.png")
        self.player = pygame.image.load("images/player.png")

        self.y_vector_angle = np.array([-0.5 * self.tile_size, 0.25 * self.tile_size])
        self.x_vector_angle = np.array([0.5 * self.tile_size, 0.25 * self.tile_size])

        self.tile_map = self.generate_tile_map()
        self.asset_map = self.generate_asset_map()

    def generate_tile_map(self):
        return [1 for _ in range(self.x_grid_count * self.y_grid_count)]

    def generate_asset_map(self):
        asset_map = [0 for _ in range(self.x_grid_count * self.y_grid_count)]
        for _ in range(10):
            asset_map[random.randint(0, len(asset_map))] = 2
        asset_map[len(asset_map) // 2 + self.x_grid_count // 2] = 3
        return asset_map

        # # Make the map
        # tile_map = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 19 -> 1
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 39 -> 1
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 59 -> 2
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 79 -> 3
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 99 -> 4
        #             1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 119 -> 5
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 139 -> 6
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 159 -> 7
        #             1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 179 -> 8
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 199 -> 9
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 219 -> 11
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 239 -> 11
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,  # 259 -> 12
        #             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0]  # 279 -> 13

    # Place images on the screen to form a map
    def draw_map(self, camera_x, camera_y, player_x, player_y):
        for index, item in enumerate(self.tile_map):
            x = ((index - (self.x_grid_count * (index // self.y_grid_count))) * self.x_vector_angle)
            y = ((index // self.x_grid_count) * self.y_vector_angle)
            result = x + y
            if item == 1:
                self.screen.blit(self.grass, ((result[0] - (self.tile_size // 2)) + self.width // 2 + camera_x,
                                              result[1] + 64 + camera_y))

        for index, asset in enumerate(self.asset_map):
            x = ((index - (self.x_grid_count * (index // self.y_grid_count))) * self.x_vector_angle)
            y = ((index // self.x_grid_count) * self.y_vector_angle)
            result = x + y
            if asset == 2:
                self.screen.blit(self.tree,
                                 ((result[0] - (self.tile_size // 2)) + self.width // 2 + camera_x,
                                  result[1] + 64 - self.tile_size + camera_y))
            elif asset == 3:
                self.screen.blit(self.player, ((result[0] - (self.tile_size // 2)) + self.width // 2 + player_x,
                                               result[1] + 64 - self.tile_size + player_y))
