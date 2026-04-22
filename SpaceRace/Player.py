from slankpy.Objects import PhysicsObject
from slankpy.Input import Input
import pygame
from . import config


class Player(PhysicsObject.PhysicsObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 5
        self.id = -1

        self.set_friction(0.1)

    def update(self) -> None:

        is_move = Input.is_key_pressed(config.PLAYER_KEYS[self.id]["spam"])
        if is_move:
            self.apply_force(0, self.speed)

        self.move_and_slide()

    
    