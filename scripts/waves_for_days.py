#!/usr/bin/python3
from pyspacelib.ft import flaschen_taschen as ftc
from math import (
    sin,
    pi,
    sqrt,
    atan
)
from time import sleep
from colorsys import hsv_to_rgb


def wave(color, phase=0, freq=0):
    w = ftc.width
    h = ftc.height
    r, g, b = color
    _norm = sqrt(w**2 + h**2)

    for x in range(w):
        for y in range(h):
            _x2 = (x-w/2)*(x-w/2)
            _y2 = (y-h/2)*(y-h/2)
            _r = sqrt(_x2 + _y2)
            intnsty = sin(freq * _r * pi/180 + ((phase * pi/180) % 360))

            ftc.set(x, y, (max(int(r*intnsty), 1),
                           max(int(g*intnsty), 1),
                           max(int(b*intnsty), 1)))
    ftc.show()


if __name__ == "__main__":
    phase = 0
    speed = 0
    t = 0
    x = 0

    while True:
        wave((255, 0, 255), phase, speed)
        factor = sin(x/10*pi/180)
        t = t + 1
        x = (t - t % 100)/100
        phase += 15
        speed = 1000 * factor
