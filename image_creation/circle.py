from image_creation.point import Point

class Circle:
    def __init__(self, canvas, x, y, radius):
        self.canvas = canvas
        self.position = Point([x,y])
        self.radius = radius