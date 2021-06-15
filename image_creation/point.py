from numpy import ndarray, asarray


class Point(ndarray):
    def __new__(cls, input_arr, **kwargs):
        point = asarray(input).view(cls)
        return point

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @x.setter
    def x(self, val):
        self[0] = val

    @y.setter
    def y(self, val):
        self[1] = val

