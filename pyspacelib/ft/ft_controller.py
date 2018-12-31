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

    min_pixel_val = 5

    def __init__(self):
        self.client = ftclient()

    def pad(self, image_width, image_height):
        self.x_pad = self.client.width - image_width
        self.y_pad = self.client.height - image_height

        self.t_pad = int(self.y_pad/2)
        self.b_pad = self.y_pad - self.t_pad
        self.l_pad = int(self.x_pad/2)
        self.r_pad = self.x_pad - self.l_pad

    def fill_buffer(self, ft_image):
        # self.image = image
        pixels = ft_image.pixels
        image_width = ft_image.width
        image_height = ft_image.height
        self.pad(image_width, image_height)
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
                    line.append((self.min_pixel_val,
                                 self.min_pixel_val,
                                 self.min_pixel_val))
                    self.client.set(col, row, (self.min_pixel_val,
                                               self.min_pixel_val,
                                               self.min_pixel_val))
                else:
                    if (
                        col - self.l_pad >= image_width or
                        row - self.t_pad >= image_height
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
