from slankpy.Objects import PhysicsObject
from slankpy.Input import Input
import pygame
import config
import random

class Player(PhysicsObject.PhysicsObject):
    def __init__(self, width:int, height:int, id:int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 15
        self.id = id

        self.set_friction(0.1)

        self.prev_keys = pygame.key.get_pressed()

        anim_rand = random.randrange(1, 3)
        if anim_rand == 1: 
            self.sprite.add_sprites("SpaceRace/assets/ships/american.png", "ship", 4, 1)
        if anim_rand == 2:
            self.sprite.add_sprites("SpaceRace/assets/ships/ussr.png", "ship", 4, 1)

        self.set_sprite("ship", 0)


        self.animation_frame = 0
        self.animation_delay_ticks = 0

    def update(self) -> None:

        self.animation_delay_ticks += 1
        if self.animation_delay_ticks == 10:
            self.animation_frame += 1
            self.animation_delay_ticks = 0
        if self.animation_frame == 3:
            self.animation_frame = 0
        self.set_sprite("ship", self.animation_frame)


        keys = pygame.key.get_pressed()

        if keys[config.PLAYER_KEYS[self.id]["spam"]] and not self.prev_keys[config.PLAYER_KEYS[self.id]["spam"]]:
            self.apply_force(0, -self.speed)

        self.prev_keys = keys
 
        if self.viewport_y >= pygame.display.get_surface().get_height():
            self.kill()

        self.move_and_slide()

    
    