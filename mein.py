import pygame as py
import spraet as sp
import karta as ka

okHo = py.display.set_mode([1000, 700])
s = 0

igrok = sp.xtk()
karta = ka.Karta()

while s == 0:
    okHo.fill([0,0,0])
    igrok.dBio()
    igrok.res(okHo)
    a=py.event.get()
    for e in a:
        if e.type == py.QUIT:
            s = 1
    py.display.update()