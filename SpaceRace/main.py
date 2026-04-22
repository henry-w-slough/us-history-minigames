from slankpy.Screen import Screen
from slankpy.Input import Input
from slankpy.Objects import PhysicsObject
from slankpy.Objects import KinematicObject
from slankpy.Camera import Camera
import pygame



screen = Screen.Screen(800, 800)
screen.set_caption("Space Race")
screen.set_fill_color((200, 200, 200))
screen.add_layer("sprites")



player = PhysicsObject.PhysicsObject(32, 32, screen.layers["sprites"])
player.set_friction(0.2)
player.image.fill((100, 100, 200)) #type: ignore

object = KinematicObject.KinematicObject(32, 32, screen.layers["sprites"])
object.image.fill((200, 100, 100)) #type: ignore
camera = Camera.Camera(player)



running = True
while running:


    move_x = Input.get_input_vector(pygame.K_a, pygame.K_d)
    move_y = Input.get_input_vector(pygame.K_w, pygame.K_s)
    player.apply_force(move_x*5, move_y*5)
    player.move_and_slide()


    if screen.has_quit():
        running = False


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()
    
