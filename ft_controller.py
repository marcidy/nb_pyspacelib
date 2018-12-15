from ft import ftclient
from PIL import Image
from image_helpers import pixelate
import os


class FTImage:
    pixelated = None

    def __init__(self, img_path, dest_path):
        self.img_path = img_path
        self.dest_path = dest_path

    def load_pixels(self):
        img = Image.open(self.pixelated)
        self.pixels = img.load()
        self.height = img.height
        self.width = img.width

    def pixelate(self, dest_path, width, height):
        if self.img_path is not None:

            ret = pixelate(self.img_path,
                           dest_path,
                           width,
                           height)
            self.pixelated = dest_path

    def load_image(self, img_path):
        name = img_path.split('/')[-1]
        self.dest_path = os.path.join(self.dest_dir, "ft-" + name)
        self.image = FTImage(img_path, dest_path)
        self.image.pixelate(dest_path,
                            self.client.width,
                            self.client.height)
        self.image.load_pixels()


class BitMap(FTImage):

    def load_pixels(self, bg=(0, 0, 0), fg=(1, 1, 1)):
        img = 1


class FTController:

    def __init__(self, dest_dir):
        self.client = ftclient()
        self.dest_dir = dest_dir

    def pad(self):
        self.x_pad = self.client.width - self.image.width
        self.y_pad = self.client.height - self.image.height

        self.t_pad = int(self.y_pad/2)
        self.b_pad = self.y_pad - self.t_pad
        self.l_pad = int(self.x_pad/2)
        self.r_pad = self.x_pad - self.l_pad

    def fill_buffer(self, pixels):
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
                    line.append((0, 0, 0))
                    self.client.set(col, row, (0, 0, 0))
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
