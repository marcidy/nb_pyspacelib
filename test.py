from ft.ft import ftclient
from math import (
    sin,
    pi,
    sqrt,
    atan
)
from time import sleep
from colorsys import hsv_to_rgb


def wave(ftc, color):
    w = ftc.width
    h = ftc.height

    for x in range(w):
        for y in range(h):
            r = sqrt((x-w/2)*(x-w/2) + (y-h/2)*(y-h/2))/sqrt(w**2 + h**2)
            intnsty = max(int(255*sin(r * pi/180)), 1)
            ftc.set(x, y, (intnsty, 0, intnsty))

    ftc.show()


def wave_test(ftc):
    w = ftc.width
    h = ftc.height

    for phase in range(2000):
        for x in range(w):
            for y in range(h):
                _x = ((x-w/2)*2)**2
                _y = ((y-h/2)*2)**2
                _r = sqrt(_x + _y)
                _int = sin(32 * _r * pi/180 + (phase % 360)/360 * pi)
                _thta = atan((x - w/2)/(y - h/2)) * phase/1000
                _h = abs(_thta)
                r, g, b = hsv_to_rgb(_h, .75, max(_int, 1/255))
                ftc.set(x, y, (int(r*255), int(g*255), int(b*255)))
        ftc.show()
