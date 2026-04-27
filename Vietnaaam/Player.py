from pygame.sprite import Group
from slankpy.Objects import KinematicObject
from slankpy.Input import Input

import pygame


class Player(KinematicObject.KinematicObject):


    def __init__(self, width: int, height: int, id:int, *groups: Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 5

        self.id = id

    
    def update(self) -> None:

        move_x = Input.get_input_vector(pygame.K_w, pygame.K_s)
        move_y = Input.get_input_vector(pygame.K_a, pygame.K_d)

        self.add_position(move_x * self.speed, move_y * self.speed)
        
