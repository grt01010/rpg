import pygame as py
import spraet as sp
import karta as ka
import seting as se
import kamera as kam

okHo = py.display.set_mode([1000, 700])
s = 0

igrok = sp.xtk()
karta = ka.Karta()

kamera = kam.Kamera(igrok)

while s == 0:
    okHo.fill([0,0,0])
    karta.res(okHo, kamera)
    kamera.cle()
    igrok.dBio()
    igrok.res(okHo)
    a=py.event.get()
    for e in a:
        if e.type == py.QUIT:
            s = 1
    py.display.update()
