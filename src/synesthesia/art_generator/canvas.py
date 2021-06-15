import numpy as np
from PIL import Image
import math


class Canvas:
    def __init__(self, height, width):
        self._canvas = np.ndarray(shape=(width, height, 4), dtype=np.uint8)
        self._canvas[:] = 255
        self.width = width
        self.height = height

    @property
    def canvas(self):
        return self._canvas

    def export(self):
        return Image.fromarray(self._canvas)

    def layer(self, arr):
        for rowIndex, row in enumerate(self.canvas):
            for colIndex, col in enumerate(row):
                self._canvas[rowIndex][colIndex] = np.array(
                    [math.floor((int(col[0]) + int(arr[rowIndex][colIndex][0])) / 2),
                     math.floor((int(col[1]) + int(arr[rowIndex][colIndex][1])) / 2),
                     math.floor((int(col[2]) + int(arr[rowIndex][colIndex][2])) / 2),
                     math.floor((int(col[3]) + int(arr[rowIndex][colIndex][3])) / 2)], dtype=np.uint8)
