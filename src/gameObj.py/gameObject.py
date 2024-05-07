from pygame.sprite import Group, Sprite, AbstractGroup
from pygame.image import load
from pygame.transform import scale, rotate
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.mask import from_surface
from src.vector import Vector2

class GameObject(Sprite):
    def __init__(
            self, 
            position:Vector2 = Vector2(),
            velocity:Vector2 = Vector2(),
            acceleration:Vector2 = Vector2(),
            angularVelocity:float = 0,
            angularAcceleration:float = 0,
            size:Vector2 = Vector2(10,10),

            image:Surface = None,
            imagePath:str = None,
            *groups: AbstractGroup) -> None:
        
        super().__init__(*groups) 

        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.angularVelocity = angularVelocity
        self.angularAcceleration = angularAcceleration
        self.size = size
        
        self.angle = 0

        if image is None:
            if imagePath is None:
                # Color rectangle
                image = Surface((size[0], size[1]),masks=(255,0,0,0.5))
            else:
                image = load(imagePath)
                
        self.origImage = scale(image, self.size.tuple())
        self.image = self.origImage
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
        self.setPosition(self.position)
    
    def setPosition(self, coordinates:Vector2)->None:
        self.rect.x, self.rect.y = self.position.tuple()
    
    def rotate(self, angle:float):
        angle %= 360
        self.angle = angle
        self.image = rotate(self.origImage, self.angle)
        self.rect = self.image.get_rect()
        self.mask = from_surface(self.image)
    
    def innerOutOfBounds(self, bounds:tuple[4]):
        return (self.position.x < bounds[0] or 
                self.position.y < bounds[1] or 
                self.position.x + self.size.x > bounds[2] or
                self.position.y + self.size.y > bounds[3])

    def outerOutOfBounds(self, bounds:tuple[4]):
        return (self.position.x + self.size.x < bounds[0] or 
                self.position.y + self.size.y < bounds[1] or 
                self.position.x > bounds[2] or
                self.position.y > bounds[3])



    