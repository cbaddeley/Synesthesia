from PIL import Image

from image_creation.cairo_helper import do_stuff
from image_creation.canvas import Canvas


def blank_image():
    canvas = Canvas(256, 256)
    return canvas.export()


def cairo_image():
    return Image.fromarray(do_stuff())


def concat():
    canvas = Canvas(256, 256)
    canvas.concatenate(do_stuff())
    return canvas.export()