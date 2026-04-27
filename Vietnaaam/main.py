from slankpy.Screen import Screen
from slankpy.Camera import Camera 
from slankpy.GameObject import GameObject
import Player


screen = Screen.Screen(800, 800)
screen.set_fill_color((100, 150, 100))

screen.add_layer("players")


player = Player.Player(32, 32, screen.layers["players"])
player.image.fill((255, 255, 255))


camera = Camera.Camera(player)


running = True
while running:


    if screen.has_quit():
        running = False

    
    camera.apply_offset(screen.layers["players"])
    screen.visible_layer = camera.cull_layers(
        screen.layers["players"]
    )

    screen.update()