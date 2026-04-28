from pygame.sprite import Group
from slankpy.Objects import KinematicObject
from slankpy.Input import Input
import Bullet as Bullet

import config
import pygame


class Player(KinematicObject.KinematicObject):


    def __init__(self, width: int, height: int, id:int, bullet_group:Group, *groups: Group) -> None:
        super().__init__(width, height, *groups)


        self.speed = 1
        self.id = id


        self.animation_frame = 0
        self.animation_delay = 0

        self.sprite.add_sprites("Vietnaaam/assets/player_walk_forward.png", "walk_forward", 8, 1)
        self.sprite.add_sprites("Vietnaaam/assets/player_walk_backward.png", "walk_backward", 8, 1)
        self.sprite.add_sprites("Vietnaaam/assets/player_walk_left.png", "walk_left", 8, 1)
        self.sprite.add_sprites("Vietnaaam/assets/player_walk_right.png", "walk_right", 8, 1)
        self.sprite.add_sprites("Vietnaaam/assets/player_hurt.png", "hurt", 1, 1)


        self.direction = "forward"

        self.prev_keys = pygame.key.get_pressed()

        self.bullet_group = bullet_group

    
    def update(self) -> None:


        self.animation_delay += 1
        if self.animation_delay >= 25:
            self.animation_frame += 1
            self.animation_delay = 0
        if self.animation_frame >= 4:
            self.animation_frame = 0
        

        move_x = Input.get_input_vector(config.PLAYER_KEYS[self.id]["left"], config.PLAYER_KEYS[self.id]["right"])
        move_y = Input.get_input_vector(config.PLAYER_KEYS[self.id]["up"], config.PLAYER_KEYS[self.id]["down"])
        self.add_position(move_x*self.speed, move_y*self.speed)

        if move_x < 0:
            self.direction = "left"
        if move_x > 0:
            self.direction = "right"
        if move_y < 0:
            self.direction = "backward"
        if move_y > 0:
            self.direction = "forward"


        self.set_sprite(f"walk_{self.direction}", self.animation_frame)


        hits = list(pygame.sprite.spritecollide(self, self.bullet_group, False)) #type: ignore
        if hits:
            if hits[0].owner != self:
                self.sprite.set_sprite("hurt", 0)
                self.health -= 1

        if self.health <= 0:
            self.kill()

        keys = pygame.key.get_pressed()
        if keys[config.PLAYER_KEYS[self.id]["spam"]] and not self.prev_keys[config.PLAYER_KEYS[self.id]["spam"]]:
            new_bullet = Bullet.Bullet(4, 4, self.direction, self, self.bullet_group)
            new_bullet.set_position(self.rect.x+(self.rect.width//2), self.rect.y)

        self.prev_keys = keys