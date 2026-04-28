import pygame

from slankpy.Objects import KinematicObject


class Bullet(KinematicObject.KinematicObject):
    def __init__(self, width: int, height: int, direction:str, owner, *groups: pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.direction = direction

        self.owner = owner

        self.speed = 10

        self.image.fill((135, 113, 0))

    def update(self) -> None:
        
        if self.direction == "forward":
            self.add_position(0, self.speed)
        if self.direction == "backward":
            self.add_position(0, -self.speed)
        if self.direction == "left":
            self.add_position(-self.speed, 0)
        if self.direction == "right":
            self.add_position(self.speed, 0)

 

    
