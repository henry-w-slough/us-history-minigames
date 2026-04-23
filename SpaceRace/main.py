from slankpy.Screen import Screen
from slankpy.Input import Input
from slankpy.Camera import Camera
from slankpy.GameObject import GameObject
import pygame
import math
import Player
import config


screen = Screen.Screen(800, 800)
screen.set_caption("Space Race")
screen.set_fill_color((200, 200, 200))
screen.add_layer("sprites")


player_distance = 128
for p in range(config.TOTAL_PLAYERS):
    
    player = Player.Player(32, 32, screen.layers["sprites"])
    player.id = len(screen.layers["sprites"])-1
    player.image.fill((100, 100, 100))

    player.set_position(player.id * player_distance, 0)


total_x = 0
for g in screen.layers.values():
    for s in g.sprites():
        total_x += s.rect.x


center = GameObject.GameObject(16, 16, screen.layers["sprites"])
center.image.fill((255, 255, 255, 150))

camera = Camera.Camera(center)

center.set_position(total_x//len(screen.layers["sprites"].sprites())+(player_distance//2-16), 0)

dist_y = 0

running = True
while running:


    total_y = 0
    for g in screen.layers.values():
        for s in g:
            total_y += s.rect.y

            if s.rect.y < 0:
                camera.set_zoom(0.5)

    center.set_position(0, total_y//len(screen.layers["sprites"].sprites())+(player_distance//2-16))

   
    if screen.has_quit():
        running = False


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()
    








