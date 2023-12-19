import pygame as py
import spraet as sp
import karta as ka
import seting as se
import kamera as kam
import npc as np
py.init()


okHo = py.display.set_mode([se.RACMERX, se.RACMERY])
s = 0

igrok = sp.xtk()
karta = ka.Karta()
npc = np.Npc(100, 500, karta.spisok_kartinok[120])


kamera = kam.Kamera(igrok)

while s == 0:
    okHo.fill([0,0,0])
    karta.res(okHo, kamera)
    npc.res(okHo, kamera)
    kamera.cle(karta.shir, karta.vis)
    igrok.dBio(karta.plitki, npc)
    igrok.res(okHo, kamera)
    npc.dbig(igrok)
    
    a=py.event.get()
    for e in a:
        if e.type == py.QUIT:
            s = 1
    py.display.update()
