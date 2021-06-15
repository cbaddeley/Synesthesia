import cairo
import numpy as np


class Context:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self._surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self._ctx = cairo.Context(self._surface)

    @property
    def ctx(self):
        return self._ctx

    def export(self):
        buf = self._surface.get_data()
        return np.ndarray(shape=(self.width, self.height, 4), dtype=np.uint8, buffer=buf)
