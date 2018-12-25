import os
from PIL import Image
from pyspacelib.ft.ft import ftclient
from pyspacelib.ft.image_helpers import pixelate


class FTImage:

    def __init__(self, img_path, dest_path):
        self.img_path = img_path
        self.name = img_path.split('/')[-1]
        self.dest_path = os.path.join(dest_path, "ft-" + self.name)

    def pixelate(self, width, height):
        if self.img_path is not None:

            ret = pixelate(self.img_path,
                           self.dest_path,
                           width,
                           height)

        img = Image.open(self.dest_path)
        self.pixels = img.load()
        self.height = img.height
        self.width = img.width


class FTController:

    def __init__(self):
        self.client = ftclient()

    def pad(self):
        self.x_pad = self.client.width - self.image.width
        self.y_pad = self.client.height - self.image.height

        self.t_pad = int(self.y_pad/2)
        self.b_pad = self.y_pad - self.t_pad
        self.l_pad = int(self.x_pad/2)
        self.r_pad = self.x_pad - self.l_pad

    def fill_buffer(self, image):
        self.image = image
        pixels = self.image.pixels
        self.pad()
        self.grid = []

        for row in range(self.client.height):
            line = []
            for col in range(self.client.width):
                if (
                    row < self.b_pad or
                    row >= (self.client.height - self.t_pad) or
                    col < self.l_pad or
                    col >= (self.client.width - self.r_pad)
                ):
                    line.append((1, 1, 1))
                    self.client.set(col, row, (1, 1, 1))
                else:
                    if (
                        col - self.l_pad >= self.image.width or
                        row - self.t_pad >= self.image.height
                    ):
                        msg = "Row: {}  -  Col: {}".format(row, col)
                        raise ValueError(msg)

                    try:
                        self.client.set(col, row, pixels[col-self.l_pad,
                                                         row-self.b_pad])
                    except IndexError:
                        msg = "row: {}, height: {} - col: {}, width: {}".format(row - self.t_pad, self.image.height, col - self.y_pad, self.image.width)  # NOQA
                        raise IndexError(msg)

                    line.append(pixels[col-self.l_pad, row-self.b_pad])

            self.grid.append(line)

    def show(self):
        self.client.show()
