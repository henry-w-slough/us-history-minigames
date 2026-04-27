from typing import Any

from slankpy.Objects import PhysicsObject
import pygame
import random


class Explosion(PhysicsObject.PhysicsObject):


    def __init__(self, width: int, height: int, *groups: pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.set_friction(0)

        self.apply_force(random.randrange(-10, 10), random.randrange(-10, -5))

        self.sprite.add_sprites("SpaceRace/assets/explosion.png", "explosion", 1, 1)
        self.set_sprite("explosion", 0)


    def update(self) -> None:

        self.viewport_y += self.vel_y
        self.viewport_x += self.vel_x

        self.move_and_slide()

        