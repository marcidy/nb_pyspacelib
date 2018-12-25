#!/usr/bin/python3
''' Randomly flashes lights with all the rgbCans.  Top stop import the universe
again and use

universe.all_off()
universe.show()
'''
from pyspacelib.dmx import universe
from pyspacelib.dmx import rgbCan
from random import randint
import time


def main():
    for id, fixture in universe.fixtures.items():
        if isinstance(fixture, rgbCan):
            fixture.strobe(randint(180, 255))
            fixture.set_rgb(randint(4, 255),
                            randint(4, 255),
                            randint(4, 255))
            universe.show()
            time.sleep(4)


if __name__ == "__main__":
    universe.all_on()
    while True:
        main()
