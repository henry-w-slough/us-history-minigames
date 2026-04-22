from slankpy.Screen import Screen
from slankpy.Input import Input
from slankpy.Camera import Camera
import pygame
import math
import Player



screen = Screen.Screen(800, 800)
screen.set_caption("Space Race")
screen.set_fill_color((200, 200, 200))
screen.add_layer("sprites")


player = Player.Player(32, 32, screen.layers["sprites"])
player.id = len(screen.layers["sprites"])-1
player.image.fill((100, 100, 100))

obj = Player.Player(32, 32, screen.layers["sprites"])
obj.id = len(screen.layers["sprites"])-1
obj.image.fill((50, 50, 50))


camera = Camera.Camera(player)


running = True
while running:


    if screen.has_quit():
        running = False



    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()
    








