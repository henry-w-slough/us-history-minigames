from slankpy.Objects import PhysicsObject
from slankpy.Input import Input
import pygame
import config
import random

class Player(PhysicsObject.PhysicsObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 5
        self.id = -1

        self.set_friction(0.1)

        self.fall_speed = random.randrange(1, 2)

        self.prev_keys = pygame.key.get_pressed()

    def update(self) -> None:

        keys = pygame.key.get_pressed()

        if keys[config.PLAYER_KEYS[self.id]["spam"]] and not self.prev_keys[config.PLAYER_KEYS[self.id]["spam"]]:
            self.apply_force(0, -self.speed)
        else:
            self.apply_force(0, self.fall_speed)

        self.prev_keys = keys
 
        if self.viewport_y >= pygame.display.get_surface().get_height():
            self.kill()

        self.move_and_slide()

    
    