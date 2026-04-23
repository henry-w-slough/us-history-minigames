from slankpy.Screen import Screen
from slankpy.Input import Input
from slankpy.Camera import Camera
from slankpy.GameObject import GameObject
import pygame
import math
import Player
import config
import random


PLAYER_WIDTH = 32
PLAYER_DISTANCE = 256

ZOOM_SCALE_FACTOR = 100
MAX_ZOOM = 2
MIN_ZOOM = 0.3


screen = Screen.Screen(800, 800)
screen.set_caption("Space Race")
screen.set_fill_color((200, 200, 200))
screen.add_layer("sprites")


for p in range(config.TOTAL_PLAYERS):
    
    player = Player.Player(PLAYER_WIDTH, PLAYER_WIDTH, screen.layers["sprites"])
    player.id = len(screen.layers["sprites"])-1
    player.image.fill((random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100)))

    player.set_position(player.id * PLAYER_DISTANCE, 0)


total_x = 0
for g in screen.layers.values():
    for s in g.sprites():
        total_x += s.rect.x


center = GameObject.GameObject(1, 1, screen.layers["sprites"])
center.set_position(total_x//len(screen.layers["sprites"].sprites())+(PLAYER_DISTANCE//2-(PLAYER_WIDTH//2)), 0)


camera = Camera.Camera(center)


running = True
while running:

    total_y = 0
    all_player_y = []
    for g in screen.layers.values():
        for s in g:
            total_y += s.rect.y
            all_player_y.append(s.rect.y)

    midpoint = total_y // len(screen.layers["sprites"].sprites()) + (PLAYER_DISTANCE // 2) - (PLAYER_WIDTH // 2)
    center.set_position(center.rect.x, midpoint)

    smallest_y = min(all_player_y)
    largest_y = max(all_player_y)

    if largest_y != 0 and smallest_y != 0:
        camera.set_zoom(1 / (largest_y - smallest_y) * ZOOM_SCALE_FACTOR)
        camera.zoom = pygame.math.clamp(camera.zoom, MIN_ZOOM, MAX_ZOOM)

    


    if screen.has_quit():
        running = False


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()
    
