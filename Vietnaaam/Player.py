from pygame.sprite import Group
from slankpy.Objects import KinematicObject
from slankpy.Input import Input

import config


class Player(KinematicObject.KinematicObject):


    def __init__(self, width: int, height: int, id:int, *groups: Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 5
        self.id = id

        self.animation_frame = 0
        self.animation_delay = 0

    
    def update(self) -> None:

        self.animation_delay += 1
        if self.animation_delay == 25:
            self.animation_frame += 1
            self.animation_delay = 0
        if self.animation_frame == 4:
            self.animation_frame = 0
        self.set_sprite("walk_forward", self.animation_frame)
        
        move_x = Input.get_input_vector(config.PLAYER_KEYS[self.id]["left"], config.PLAYER_KEYS[self.id]["right"])
        move_y = Input.get_input_vector(config.PLAYER_KEYS[self.id]["up"], config.PLAYER_KEYS[self.id]["down"])
        self.add_position(move_x*self.speed, move_y*self.speed)