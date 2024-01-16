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
esa= py.time.Clock()

kamera = kam.Kamera(igrok)
sd = 0
pober = py.surface.Surface([10000000000000000000000000000000000000000000000000,10000000000000000000000000000000000000000000000000], py.SRCALPHA)
ads=255

while s == 0:
    ads=ads-1
    okHo.fill([0,0,0])
    karta.res(okHo, kamera)
    pober.fill([250,250,250,ads])
    okHo.blit(pober,[1,1])
    npc.res(okHo, kamera)
    kamera.cle(karta.shir, karta.vis)
    igrok.dBio(karta.plitki, npc, sd)
    igrok.res(okHo, kamera)
    npc.dbig(igrok,sd)
    h = str(esa.get_fps())

    py.display.set_caption(h)
    
    a=py.event.get()
    for e in a:
        if e.type == py.QUIT:
            s = 1
    py.display.update()
    sd = esa.tick(60)
    print(sd)