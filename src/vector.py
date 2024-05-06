from math import atan2, hypot, pi

class Vector2:
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y

    def toAngle(self, degrees = False)->float:
        radiants =  atan2(self.y, self.x)
        return radiants * 180 / pi if degrees else radiants
    
    def module(self)->float:
        return hypot(self.x, self.y)
    
    # =
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # !=
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    # +
    def __add__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("Expected \"Vector2\" found \"{}\" instead".format(type(other)))
        return Vector2(self.x + other.x, self.y + other.y)
    # -
    def __sub__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("Expected \"Vector2\" found \"{}\" instead".format(type(other)))
        return Vector2(self.x - other.x, self.y - other.y)
    # *
    def __mul__(self, factor:float|int):
        if isinstance(factor, float) or isinstance(factor, int):
            # multiply
            return Vector2(self.x * factor, self.y * factor)
        else:
            raise TypeError("Expected \"factor\" to be of type \"float\" or \"int\": found \"{}\" instead".format(type(factor)))
    # /
    def __truediv__(self, factor:float|int):
        if isinstance(factor, float) or isinstance(factor, int):
            # division
            return Vector2(self.x / factor, self.y / factor)
        else:
            raise TypeError("factor has to be \"float\" or \"int\": found {} instead".format(type(factor)))
    # //
    def __floordiv__(self, factor:float|int):
        if isinstance(factor, float) or isinstance(factor, int):
            # division
            return Vector2(self.x // factor, self.y // factor)
        else:
            raise TypeError("factor has to be \"float\" or \"int\": found {} instead".format(type(factor)))
    
    def __getitem__(self, key:int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise KeyError("Key invalid")
        
    def tuple(self)->tuple[2]:
        return (self.x, self.y)

    def __str__(self)->str:
        return "({}, {})".format(self.x, self.y)
    
    