#!/usr/bin/python3

from ft import ftclient

ftc = ftclient(transparent=False)

for y in range(ftc.height):
    for x in range(ftc.width):
        ftc.set(x, y, (0, 0, 1))

ftc.show()
