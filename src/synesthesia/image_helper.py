import numpy as np
from PIL import Image


def create_image_array(x, y):
    return np.zeros([x, y, 3], dtype=np.uint8)


def create_image_from_array(image_array):
    return Image.fromarray(image_array)

