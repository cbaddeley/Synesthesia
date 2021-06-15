from math import pi


class Circle:
    def __init__(self, context, x, y, radius):
        self._context = context
        self._position = (x, y)
        self._radius = radius

    @property
    def context(self):
        return self._context

    @property
    def position(self):
        return self._position

    @property
    def radius(self):
        return self.radius

    def draw(self):
        self._context.ctx.arc(self._position[0], self._position[1], self._radius, 0, pi*2)
        self._context.ctx.fill()
