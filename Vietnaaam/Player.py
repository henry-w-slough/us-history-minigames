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

        if Input.is_key_pressed(   ):
        
