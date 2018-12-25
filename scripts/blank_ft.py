#!/usr/bin/python3

from pyspacelib.ft import flaschen_taschen as ft

for y in range(ft.height):
    for x in range(ft.width):
        ft.set(x, y, (5, 5, 5))

ft.show()
